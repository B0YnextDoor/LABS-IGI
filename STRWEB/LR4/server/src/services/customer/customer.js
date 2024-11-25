import { OrderService } from "../order/order.js";
import { Customer } from "../../models/customer.js";
import { hashPassword } from "../../core/security.js";
import { CONFIG } from "../../core/config.js";
import uuid4 from "uuid4";

export class CustomerService {
  orderService = new OrderService();
  _select = "-__v -created_at -updated_at";

  async getAll() {
    return await Customer.find({}, `${this._select} -password`);
  }

  async getById(id, withPassword = false) {
    const user = await Customer.findById(
      id,
      `${this._select}${withPassword ? "" : " -password"}`
    );
    if (!user) null;
    return { ...user.toObject(), role: CONFIG.ROLES.CUSTOMER };
  }

  async getOrders(id) {
    if (!(await this.getById(id))) return "Customer doesn't exist";
    return await this.orderService.getByCustomer(id);
  }

  async getByEmail(email) {
    return await Customer.findOne({ email: email });
  }

  async getByPhone(phone) {
    return await Customer.findOne({ phone: phone });
  }

  async create(data) {
    if (await this.getByEmail(data.email))
      return "User with this email already exists";
    if (data.phone && (await this.getByPhone(data.phone)))
      return "User with this phone already exists";
    data.password ??= uuid4();
    const hashed_password = await hashPassword(data.password);
    try {
      const new_user = new Customer({ ...data, password: hashed_password });
      await new_user.save();
      return new_user.toObject();
    } catch (e) {
      console.log(e);
      return null;
    }
  }

  async update(id, data) {
    const db_user = await this.getById(id, true);
    if (!db_user) return "User doesn't exist!";
    let user = await this.getByEmail(data.email);
    if (user && !user._id.equals(db_user._id))
      return "User with this email already exists";
    user = await this.getByPhone(data.phone);
    if (user && !user._id.equals(db_user._id))
      return "User with this phone already exists";
    const hashed_password = data.password
      ? await hashPassword(data.password)
      : db_user.password;
    try {
      const upd_user = await Customer.findByIdAndUpdate(
        id,
        { ...data, password: hashed_password },
        { new: true }
      );
      return upd_user ? upd_user.toObject() : "Update error!";
    } catch (e) {
      console.log(e);
      return null;
    }
  }
}
