import { Schema, model } from "mongoose";
import { Order } from "./order.js";

const customerSchema = new Schema(
  {
    name: {
      type: String,
      required: true,
    },
    phone: {
      type: String,
      default: "Not specified",
    },
    email: {
      type: String,
      required: true,
      unique: true,
    },
    password: {
      type: String,
      required: true,
    },
  },
  {
    timestamps: { createdAt: "created_at", updatedAt: "updated_at" },
    collection: "customers",
  }
);

customerSchema.pre("findOneAndDelete", async function (next) {
  try {
    const customer = await this.model.findOne(this.getFilter());
    if (customer) {
      await Review.deleteMany({ customer: customer._id });
      await Order.deleteMany({ customer: customer._id });
    }
    next();
  } catch (error) {
    next(error);
  }
});

const reviewSchema = new Schema(
  {
    rate: {
      type: Number,
      default: 1,
      min: 1,
      max: 5,
    },
    text: {
      type: String,
      required: true,
    },
    customer: {
      type: Schema.Types.ObjectId,
      ref: "Customer",
      required: true,
    },
  },
  {
    timestamps: { createdAt: "created_at", updatedAt: "updated_at" },
    collection: "reviews",
  }
);

export const Customer = model("Customer", customerSchema);
export const Review = model("Review", reviewSchema);
