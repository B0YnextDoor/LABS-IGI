import { Review } from "../../models/customer.js";
import { CustomerService } from "./customer.js";

export class ReviewService {
  customerService = new CustomerService();
  _select = "-__v -created_at";

  async getAll() {
    return await Review.find({}, this._select)
      .populate("customer", "name")
      .sort({ updated_at: -1 });
  }

  async getById(id) {
    return await Review.findById(id, this._select);
  }

  async create(data, user_id) {
    if (!(await this.customerService.getById(user_id)))
      return "User doesn't exist!";
    try {
      const new_review = new Review({ ...data, customer: user_id });
      await new_review.save();
      return new_review;
    } catch (e) {
      console.log(e);
      return null;
    }
  }

  async update(id, data, user_id) {
    if (!(await this.customerService.getById(user_id)))
      return "User doesn't exist!";
    try {
      const upd_review = await this.getById(id);
      if (!upd_review) return "Review doesn't exist!";
      else if (!upd_review.customer._id.equals(user_id))
        return "Only creator can update the review!";
      upd_review.rate = data.rate;
      upd_review.text = data.text;
      await upd_review.save();
      return upd_review;
    } catch (e) {
      console.log(e);
      return null;
    }
  }

  async delete(id, user_id) {
    try {
      const del_review = await this.getById(id);
      if (!del_review) return "Review doesn't exist";
      else if (!del_review.customer._id.equals(user_id))
        return "Only creator can delete the review!";
      await del_review.deleteOne();
      return del_review;
    } catch (e) {
      console.log(e);
      return null;
    }
  }
}
