import { Schema, model } from "mongoose";

const orderSchema = new Schema(
  {
    customer: {
      type: Schema.Types.ObjectId,
      ref: "Customer",
      required: true,
    },
    books: [
      {
        type: Schema.Types.ObjectId,
        ref: "OrderItem",
      },
    ],
    orderInfo: {
      type: Schema.Types.ObjectId,
      ref: "OrderInfo",
    },
  },
  {
    timestamps: { createdAt: "created_at", updatedAt: "updated_at" },
    collection: "orders",
  }
);

orderSchema.pre("findOneAndDelete", async function (next) {
  try {
    const order = await this.model.findOne(this.getFilter());
    if (order) {
      await mongoose.model("OrderItem").deleteMany({ order: order._id });
      await mongoose.model("OrderInfo").deleteOne({ order: order._id });
    }
    next();
  } catch (error) {
    next(error);
  }
});

const orderItemSchema = new Schema(
  {
    order: {
      type: Schema.Types.ObjectId,
      ref: "Order",
      required: true,
    },
    book: {
      type: Schema.Types.ObjectId,
      ref: "Book",
      required: true,
    },
    amount: {
      type: Number,
      default: 1,
      required: true,
    },
  },
  {
    timestamps: { createdAt: "created_at", updatedAt: "updated_at" },
    collection: "order_items",
  }
);

const orderInfoSchema = new Schema(
  {
    order: {
      type: Schema.Types.ObjectId,
      ref: "Order",
      required: true,
      unique: true,
    },
    status: {
      type: Number,
      default: 1,
    },
    sale: {
      type: Number,
      default: 0,
    },
    deliveryDate: {
      type: Date,
      required: true,
    },
    deliveryAddress: {
      type: String,
      required: true,
    },
    totalPrice: {
      type: Schema.Types.Decimal128,
      required: true,
    },
  },
  {
    timestamps: { createdAt: "created_at", updatedAt: "updated_at" },
    collection: "order_infos",
  }
);

export const Order = model("Order", orderSchema);
export const OrderItem = model("OrderItem", orderItemSchema);
export const OrderInfo = model("OrderInfo", orderInfoSchema);
