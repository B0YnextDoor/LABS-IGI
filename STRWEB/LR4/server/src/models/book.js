import { Schema, model } from "mongoose";
import { OrderItem } from "./order.js";

const authorSchema = new Schema(
  {
    name: {
      type: String,
      required: true,
      description: "Author's name",
    },
    surname: {
      type: String,
      required: true,
      description: "Author's surname",
    },
  },
  {
    timestamps: { createdAt: "created_at", updatedAt: "updated_at" },
    collection: "authors",
  }
);

authorSchema.pre("findOneAndDelete", async function (next) {
  const query = this;
  try {
    const doc = await query.model.findOne(query.getFilter());
    if (doc) {
      await mongoose.model("Book").deleteMany({ author: doc._id });
    }
    next();
  } catch (err) {
    next(err);
  }
});

const genreSchema = new Schema(
  {
    name: {
      type: String,
      required: true,
      unique: true,
      description: "Genre's name",
    },
  },
  {
    timestamps: { createdAt: "created_at", updatedAt: "updated_at" },
    collection: "genres",
  }
);

genreSchema.pre("findOneAndDelete", async function (next) {
  const query = this;
  try {
    const genreToDelete = await query.model.findOne(query.getFilter());
    if (genreToDelete) {
      const defaultGenre = await mongoose
        .model("Genre")
        .findOne({ name: "Роман" });
      if (defaultGenre) {
        await mongoose
          .model("Book")
          .updateMany(
            { genre: genreToDelete._id },
            { $set: { genre: defaultGenre._id } }
          );
      }
    }
    next();
  } catch (err) {
    next(err);
  }
});

const bookSchema = new Schema(
  {
    title: {
      type: String,
      required: true,
      description: "Book's title",
    },
    price: {
      type: Number,
      required: true,
      description: "Book's price",
    },
    amount: {
      type: Number,
      required: true,
      min: 0,
      description: "Amount of copies in the shop",
    },
    genre: {
      type: Schema.Types.ObjectId,
      ref: "Genre",
      required: true,
      default: "Роман",
    },
    author: {
      type: Schema.Types.ObjectId,
      ref: "Author",
      required: true,
    },
  },
  {
    timestamps: { createdAt: "created_at", updatedAt: "updated_at" },
    collection: "books",
  }
);

bookSchema.pre("findOneAndDelete", async function (next) {
  try {
    const book = await this.model.findOne(this.getFilter());

    if (book) {
      const isBookInOrders = await OrderItem.exists({ book: book._id });

      if (isBookInOrders) {
        const error = new Error(
          "Невозможно удалить книгу, так как она используется в заказах."
        );
        return next(error);
      }
    }
    next();
  } catch (error) {
    next(error);
  }
});

bookSchema.index({ title: 1 });
authorSchema.index({ surname: 1 });
genreSchema.index({ name: 1 });

export const Author = model("Author", authorSchema);
export const Genre = model("Genre", genreSchema);
export const Book = model("Book", bookSchema);
