import { Genre } from "../../models/book.js";

export class GenreService {
  _select = "_id name";

  async getAll() {
    return await Genre.find({}, this._select);
  }

  async getById(id) {
    return await Genre.findById(id, this._select);
  }

  async create(genre) {
    try {
      const new_genre = new Genre({ ...genre });
      await new_genre.save();
      return new_genre;
    } catch (e) {
      console.log(e);
      return null;
    }
  }

  async update(id, genre) {
    try {
      const upd_genre = await Genre.findByIdAndUpdate(
        id,
        { ...genre },
        { new: true }
      );
      return upd_genre ? this.getById(id) : "not found";
    } catch (e) {
      console.log(e);
      return null;
    }
  }

  async delete(id) {
    try {
      const del_genre = await Genre.findByIdAndDelete(id);
      return del_genre ? del_genre.toObject() : "not found";
    } catch (e) {
      console.log(e);
      return null;
    }
  }
}
