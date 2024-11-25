import { Router } from "express";
import { CustomerService } from "../../services/customer/customer.js";
import { EmployeeService } from "../../services/employee/employee.js";
import {
  checkMiddleware,
  checkRoleMiddleware,
  getUserMiddleware,
} from "../../middleware/base.js";
import { validateUserBody, validateInfoBody } from "../../middleware/user.js";
import { CONFIG } from "../../core/config.js";

export const userRouter = Router();
const customerService = new CustomerService();
const employeeService = new EmployeeService();

userRouter.use("/", (req, res, next) => {
  checkRoleMiddleware(req, res, next, CONFIG.ROLES.CUSTOMER);
});

userRouter.get("/profile", async (req, res) => {
  const { id, role } = getUserMiddleware(req);
  if (!id || !Object.values(CONFIG.ROLES).includes(role))
    res.status(403).json("bad roken");
  else if (role == CONFIG.ROLES.CUSTOMER) {
    const customer = await customerService.getById(id);
    res.status(customer ? 200 : 401).json(customer);
  } else {
    const employee = await employeeService.getProfile(id);
    res.status(employee ? 200 : 401).json(employee);
  }
});

userRouter.get("/orders", async (req, res) => {
  const { id, role } = getUserMiddleware(req);
  if (!id || role != CONFIG.ROLES.CUSTOMER) res.status(403).json("forbidden");
  else {
    const customerOrders = await customerService.getOrders(id);
    const code = typeof customerOrders === "string" ? 401 : 200;
    res.status(code).json(customerOrders);
  }
});

userRouter.use(
  "/update",
  (req, res, next) => {
    checkMiddleware(req, res, next, validateUserBody);
  },
  (req, res, next) => {
    checkMiddleware(req, res, next, validateInfoBody);
  }
);

userRouter.put("/update", async (req, res) => {
  const { id, role } = getUserMiddleware(req);
  if (!id || !Object.values(CONFIG.ROLES).includes(role))
    return res.status(403).json("bad token");
  if (role != CONFIG.ROLES.CUSTOMER) {
    const employee = await employeeService.update(id, req.body);
    const code = !employee || typeof employee == "string" ? 400 : 200;
    res.status(code).json(code == 400 ? employee : "profile updated");
  } else {
    const customer = await customerService.update(id, req.body);
    const code = !customer || typeof customer == "string" ? 400 : 200;
    res.status(code).json(code == 400 ? customer : "profile updated");
  }
});
