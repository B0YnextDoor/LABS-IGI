import { Author } from "../../models/book.js";

export class AuthorService {
  _select = "_id name surname";

  async getAll() {
    return await Author.find({}, this._select);
  }

  async getById(id) {
    return await Author.findById(id, this._select);
  }

  async create(author) {
    try {
      const new_author = new Author({ ...author });
      await new_author.save();
      return new_author;
    } catch (e) {
      console.log(e);
      return null;
    }
  }

  async update(id, author) {
    try {
      const upd_author = await Author.findByIdAndUpdate(
        id,
        { ...author },
        { new: true }
      );
      return upd_author ? this.getById(id) : "not found";
    } catch (e) {
      console.log(e);
      return null;
    }
  }

  async delete(id) {
    try {
      const del_author = await Author.findByIdAndDelete(id);
      return del_author ? del_author.toObject() : "not found";
    } catch (e) {
      console.log(e);
      return null;
    }
  }
}
