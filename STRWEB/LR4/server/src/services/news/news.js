import { News } from "../../models/news.js";

export class NewsService {
  _select = "-__v -updated_at";
  _default = "src/static/news/default.png";

  async getAll() {
    return await News.find({}, this._select).sort({ created_at: -1 });
  }

  async getById(id) {
    return await News.findById(id, this._select);
  }

  async create(data) {
    try {
      const new_news = new News({
        ...data,
        imagePath: data?.imagePath || this._default,
      });
      await new_news.save();
      return new_news;
    } catch (e) {
      console.log(e);
      return null;
    }
  }

  async update(id, data) {
    try {
      const upd_news = await this.getById(id);
      if (!upd_news) return "News doesn't exist";
      upd_news.title = data.title;
      upd_news.text = data.text;
      upd_news.imagePath = data.imagePath || upd_news.imagePath;
      await upd_news.save();
      return upd_news;
    } catch (e) {
      console.log(e);
      return null;
    }
  }

  async delete(id) {
    try {
      const del_news = await News.findByIdAndDelete(id);
      return del_news ? del_news : "News doesn't exist";
    } catch (e) {
      console.log(e);
      return null;
    }
  }
}
