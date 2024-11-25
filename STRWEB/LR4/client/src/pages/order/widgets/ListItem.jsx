import { useCallback } from "react";
import { CONFIG } from "../../../config/config";
import { useUpdateOrder } from "../hooks/useUpdateOrder";
import { OrderInfo } from "./OrderInfo";
import { getBookIds } from "../../../utils/order";

export const ListItem = ({ order, idx }) => {
  const { update, isUpdating } = useUpdateOrder(order._id, true);
  const onUpdate = useCallback(
    () =>
      update({
        status: CONFIG.ORDER_STATUS.ACTIVE,
        book_ids: getBookIds(order.books),
      }),
    [order]
  );
  return (
    <div className="order-item list-item">
      <h2>Order #{idx}</h2>
      <div className="order-item list-item">
        <h3>Customer</h3>
        <h4>Name: {order.customer.name}</h4>
        <h4>Phone: {order.customer.phone}</h4>
        <h4>Email: {order.customer.email}</h4>
      </div>
      <div className="order-books">
        {order.books.map((item, idx) => (
          <div className="order-item list-item" key={idx}>
            <h3>Book #{idx + 1}</h3>
            <h4 className="title">Title: {item.book.title}</h4>
            <h4>
              Author: {item.book.author.surname} {item.book.author.name}
            </h4>
            <h4>Genre: {item.book.genre.name}</h4>
            <h4>Price: {item.book.price}</h4>
            <h4>Amount: {item.amount}</h4>
          </div>
        ))}
      </div>
      <OrderInfo order={order} />
      {order.orderInfo.status === CONFIG.ORDER_STATUS.PENDING && (
        <div className="approve-order">
          <button
            className="btn btn-admin"
            onClick={onUpdate}
            disabled={isUpdating}
          >
            Ready to Deliver
          </button>
        </div>
      )}
    </div>
  );
};
