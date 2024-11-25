import { CONFIG } from "../../core/config.js";
import { hashPassword } from "../../core/security.js";
import { Employee, EmployeeInfo } from "../../models/employee.js";

export class EmployeeService {
  _limit = 3;
  _select = "-__v -createdAt -updatedAt";
  _default = "src/static/employees/default.jpg";

  async getAll() {
    return await Employee.find({}, this._select).populate(
      "info",
      `${this._select} -employee`
    );
  }

  async getById(id) {
    return await Employee.findById(id, this._select).populate(
      "info",
      `${this._select} -employee`
    );
  }

  async getProfile(id) {
    const employee = await this.getById(id);
    if (!employee) return null;
    return {
      role: employee.isAdmin ? CONFIG.ROLES.ADMIN : CONFIG.ROLES.EMPLOYEE,
      _id: employee._id,
      email: employee.email,
      name: employee.info.name,
      phone: employee.info.phone,
    };
  }

  async getByEmail(email) {
    return await Employee.findOne({ email: email }, this._select);
  }

  async getByPhone(phone) {
    return await EmployeeInfo.findOne({ phone: phone }, this._select);
  }

  async getInfo(filter = "", order = "name", page = 1) {
    let dir = 1;
    if (order[0] == "-") {
      dir = -1;
      order = order.slice(1);
    }
    if (!["name", "email", "phone", "description"].includes(order)) {
      order = "name";
      dir = 1;
    }
    if (["name", "phone", "description"].includes(order))
      order = "info." + order;
    const regex = filter ? new RegExp(filter.trim(), "i") : null;
    const employees = await Employee.aggregate([
      {
        $match: {
          isAdmin: false,
        },
      },
      {
        $lookup: {
          from: "employee_infos",
          localField: "info",
          foreignField: "_id",
          as: "info",
        },
      },
      {
        $unwind: "$info",
      },
      {
        $match: regex
          ? {
              $or: [
                { email: regex },
                { "info.name": regex },
                { "info.phone": regex },
                { "info.description": regex },
              ],
            }
          : {},
      },
      {
        $sort: { [order]: dir },
      },
      {
        $project: {
          __v: 0,
          createdAt: 0,
          updatedAt: 0,
          isAdmin: 0,
          "info.__v": 0,
          "info.createdAt": 0,
          "info.updatedAt": 0,
          "info.employee": 0,
        },
      },
    ]);
    const total = employees.length ?? 0;
    return {
      employees: employees.slice((page - 1) * this._limit, this._limit * page),
      total,
    };
  }

  async create(data) {
    if (await this.getByEmail(data.email))
      return "Employee with this email already exists!";
    if (await this.getByPhone(data.phone))
      return "Employee with this phone already exists!";
    const hashed_password = await hashPassword(data.password);
    try {
      const newEmployee = await Employee.create({
        email: data.email,
        password: hashed_password,
        isAdmin: !!data.isAdmin || false,
      });
      const employeeInfo = await EmployeeInfo.create({
        name: data.name,
        phone: data.phone,
        imagePath: data.imagePath || this._default,
        description: data.description || "Very important employee",
        employee: newEmployee._id,
      });
      newEmployee.info = employeeInfo._id;
      await newEmployee.save();
      return { ...newEmployee.toObject(), info: employeeInfo.toObject() };
    } catch (e) {
      console.error(e);
      return null;
    }
  }

  async update(id, data) {
    const db_employee = await this.getById(id);
    if (!db_employee) return "Employee not found!";
    let emp = await this.getByEmail(data.email);
    if (emp && !emp._id.equals(id))
      return "Employee with this email already exists!";
    emp = await this.getByPhone(data.phone);
    if (emp && !emp.employee._id.equals(id))
      return "Employee with this phone already exists!";
    const hashed_password = data.password
      ? await hashPassword(data.password)
      : db_employee.password;
    try {
      const upd_employee = await Employee.findByIdAndUpdate(
        id,
        {
          email: data.email || db_employee.email,
          password: hashed_password,
        },
        { new: true }
      );
      if (!upd_employee) throw new Error("Update error!");
      const upd_info = await EmployeeInfo.findByIdAndUpdate(
        upd_employee.info,
        {
          name: data.name || db_employee.info.name,
          phone: data.phone || db_employee.info.phone,
          imagePath: data.imagePath || db_employee.info.imagePath,
          description: data.description || db_employee.info.description,
        },
        { new: true }
      );
      if (!upd_info) throw new Error("Update error!");
      return { ...upd_employee.toObject(), info: upd_info.toObject() };
    } catch (e) {
      console.error(e);
      return null;
    }
  }

  async delete(id) {
    try {
      const del_emp = await Employee.findByIdAndDelete(id);
      return del_emp || "Employee doesn't exist!";
    } catch (e) {
      console.log(e);
      return null;
    }
  }
}
