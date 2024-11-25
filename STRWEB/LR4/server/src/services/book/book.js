import { Book } from "../../models/book.js";
import { AuthorService } from "./author.js";
import { GenreService } from "./genre.js";

export class BookService {
  _select = "";
  _orderBy = ["price", "amount"];
  _limit = 3;
  _select = "-__v -created_at -updated_at";
  authorService = new AuthorService();
  genreService = new GenreService();

  async getCatalog() {
    return await Book.find({}, this._select)
      .populate("author", "name surname")
      .populate("genre", "name")
      .sort({ amount: -1 });
  }

  async getAll(title = "", order = "amount", page = 1) {
    if (title === "all") return this.getCatalog();
    order = this._orderBy.includes(order) ? order : this._orderBy[1];
    const books = await Book.find(
      title ? { title: { $regex: title, $options: "i" } } : {},
      this._select
    )
      .populate("author", "name surname")
      .populate("genre", "name")
      .sort({ [order]: -1 });
    const total = books.length ?? 0;
    return {
      books: books.slice((page - 1) * this._limit, this._limit * page),
      total,
    };
  }

  async getById(id) {
    if (!id) return null;
    return await Book.findById(id, this._select)
      .populate("author", "name surname")
      .populate("genre", "name");
  }

  async create(book) {
    if (!(await this.genreService.getById(book.genre)))
      return "Genre doesn't exist!";
    if (!(await this.authorService.getById(book.author)))
      return "Author doesn't exist!";
    try {
      const new_book = new Book({ ...book });
      await new_book.save();
      return new_book;
    } catch (e) {
      console.log(e);
      return null;
    }
  }

  async update(id, book) {
    if (!(await this.genreService.getById(book.genre)))
      return "Genre doesn't exist!";
    if (!(await this.authorService.getById(book.author)))
      return "Author doesn't exist!";
    try {
      const upd_book = await Book.findByIdAndUpdate(
        id,
        { ...book },
        { new: true }
      );
      return upd_book ? this.getById(id) : "Book not found";
    } catch (e) {
      console.log(e);
      return null;
    }
  }

  async updateBooksAmount(items) {
    if (!items || !items.length) return "ok";
    try {
      await Promise.all(
        items.map(async (item) =>
          item.amount > 0
            ? await Book.findByIdAndUpdate(item.book, { amount: item.amount })
            : null
        )
      );
      return "ok";
    } catch (e) {
      console.log(e);
      return null;
    }
  }

  async delete(id) {
    try {
      const del_book = await Book.findByIdAndDelete(id);
      return del_book ? del_book.toObject() : "Book not found";
    } catch (e) {
      console.log(e);
      return null;
    }
  }
}
