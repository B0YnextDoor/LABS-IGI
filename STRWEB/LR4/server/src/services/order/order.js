import { CONFIG } from "../../core/config.js";
import { BookService } from "../book/book.js";
import { CartService } from "./cart.js";
import { Order, OrderInfo, OrderItem } from "../../models/order.js";
import { populate } from "dotenv";

export class OrderService {
  bookService = new BookService();
  cartService = new CartService();

  _select = "-__v -updated_at";

  async updateOrdersStatus(customerId = null) {
    const orders = await Order.aggregate([
      {
        $match: customerId ? { customer: customerId } : {},
      },
      {
        $lookup: {
          from: "order_infos",
          localField: "orderInfo",
          foreignField: "_id",
          as: "orderInfo",
        },
      },
      {
        $unwind: "$orderInfo",
      },
      {
        $match: {
          "orderInfo.status": {
            $in: [CONFIG.ORDER_STATUS.PENDING, CONFIG.ORDER_STATUS.ACTIVE],
          },
          "orderInfo.deliveryDate": { $lte: new Date() },
        },
      },
      {
        $project: {
          "orderInfo.status": 1,
          "orderInfo.deliveryDate": 1,
        },
      },
    ]);
    const ids = orders.map((order) => order._id);
    await OrderInfo.updateMany(
      { order: { $in: ids } },
      { $set: { status: CONFIG.ORDER_STATUS.DELIVERED } }
    );
  }

  async getAllOrders(status = null) {
    this.updateOrdersStatus();
    const filter = status ? { "orderInfo.status": status } : {};
    return await Order.find(filter, this._select)
      .populate("customer", "name email phone")
      .populate("orderInfo", `${this._select} -order`)
      .populate({
        path: "books",
        populate: {
          path: "book",
          populate: [
            {
              path: "author",
              select: `name surname`,
            },
            {
              path: "genre",
              select: "name",
            },
          ],
          select: `${this._select} -amount`,
        },
        select: `${this._select} -order`,
      })
      .sort({ updated_at: -1 });
  }

  async getByCustomer(id) {
    await this.updateOrdersStatus(id);
    return await Order.find({ customer: id }, `${this._select} -customer`)
      .populate("orderInfo", `${this._select} -order`)
      .sort({ updated_at: -1 });
  }

  async getOrderById(id) {
    return await Order.findById(id, this._select)
      .populate({
        path: "books",
        populate: {
          path: "book",
          populate: [
            {
              path: "author",
              select: `name surname`,
            },
            {
              path: "genre",
              select: "name",
            },
          ],
          select: `${this._select} -created_at`,
        },
        select: `${this._select} -order -created_at`,
      })
      .populate("orderInfo", `${this._select} -order -created_at`);
  }

  formOrderItems(formedCart) {
    return Object.entries(formedCart).map(([bookId, amount]) => ({
      book: bookId,
      amount,
    }));
  }

  async formOrderData(items) {
    const itemData = await Promise.all(
      items.map(async (item) => {
        const book = await this.bookService.getById(item.book);
        if (!book) return { price: 0, bookData: { book: null, amount: 0 } };
        return {
          price: Number(book.price) * item.amount,
          bookData: { book: item.book, amount: book.amount - item.amount },
        };
      })
    );
    const totalPrice = itemData.reduce((total, item) => total + item.price, 0);
    const updatedAmount = itemData.map((item) => item.bookData);
    return { totalPrice, updatedAmount };
  }

  async createOrder(customerId, orderData, cart) {
    const formedCart = this.cartService.formCart(cart);
    if (!formedCart || Object.keys(formedCart).length === 0)
      return "Cart is empty!";
    const orderItems = this.formOrderItems(formedCart);
    const { totalPrice, updatedAmount } = await this.formOrderData(orderItems);
    const sale = Number(orderData.sale ?? 0);
    try {
      if (!(await this.bookService.updateBooksAmount(updatedAmount)))
        return "Creating error";
      const order = await Order.create({
        customer: customerId,
      });
      const orderInfo = await OrderInfo.create({
        order: order._id,
        sale: sale,
        deliveryDate: String(orderData.deliveryDate),
        deliveryAddress: String(orderData.deliveryAddress),
        totalPrice: totalPrice * (1 - sale / 100),
      });
      order.orderInfo = orderInfo._id;
      const orderItemsDocs = orderItems.map((item) => ({
        ...item,
        order: order._id,
      }));
      const createdOrderItems = await OrderItem.insertMany(orderItemsDocs);
      order.books = createdOrderItems.map((item) => item._id);
      await order.save();
      return { ...order.toObject(), info: orderInfo, books: createdOrderItems };
    } catch (e) {
      console.log(e);
      return null;
    }
  }

  async returnOrderItems(orderItems) {
    return Promise.all(
      orderItems.map(async (item) => {
        const book = await this.bookService.getById(item.book);
        if (!book) return { book: null, amount: 0 };
        return { ...item, amount: book.amount + item.amount };
      })
    );
  }

  async updateOrder(id, orderData) {
    const dbOrder = await this.getOrderById(id);
    if (!dbOrder) return "Order doesn't exist";
    if (
      [CONFIG.ORDER_STATUS.DELIVERED, CONFIG.ORDER_STATUS.CANCELED].includes(
        dbOrder.orderInfo.status
      )
    )
      return "Can't update delivered/cancelled order!";
    else if (
      dbOrder.orderInfo.status == CONFIG.ORDER_STATUS.ACTIVE &&
      orderData.status != CONFIG.ORDER_STATUS.CANCELED
    )
      return "Order is in delivery you can only cancell it!";
    const items = this.cartService.formCart(orderData.book_ids);
    const orderItems = this.formOrderItems(items);
    if (orderItems.length === 0) return "Updating order error!";
    const orderBooks = dbOrder.books.map((book) => ({
      book: book.book._id,
      amount: book.amount,
    }));
    try {
      if (
        !(await this.bookService.updateBooksAmount(
          await this.returnOrderItems(orderBooks)
        ))
      )
        throw new Error("Update error!");
      const { totalPrice, updatedAmount } = await this.formOrderData(
        orderItems
      );
      if (!(await this.bookService.updateBooksAmount(updatedAmount)))
        throw new Error("Update error!");
      await OrderItem.deleteMany({ order: dbOrder._id });
      const orderItemsDocs = orderItems.map((item) => ({
        ...item,
        order: dbOrder._id,
      }));
      const createdOrderItems = await OrderItem.insertMany(orderItemsDocs);
      const sale = Number(orderData.sale ?? dbOrder.orderInfo.sale);
      const orderInfo = await OrderInfo.findByIdAndUpdate(
        dbOrder.orderInfo._id,
        {
          status: Number(orderData.status ?? dbOrder.orderInfo.status),
          sale: sale,
          deliveryAddress: String(
            orderData.deliveryAddress ?? dbOrder.orderInfo.deliveryAddress
          ),
          deliveryDate:
            orderData.deliveryDate ?? dbOrder.orderInfo.deliveryDate,
          totalPrice:
            totalPrice * (1 - sale / 100) || dbOrder.orderInfo.totalPrice,
        },
        { new: true }
      );
      if (!orderInfo) throw new Error("Update error!");
      dbOrder.books = createdOrderItems.map((item) => item._id);
      await dbOrder.save();
      return {
        ...dbOrder.toObject(),
        orderInfo: orderInfo.toObject(),
        books: createdOrderItems,
      };
    } catch (e) {
      console.log(e);
      return null;
    }
  }
}
