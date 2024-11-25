import { Router } from "express";
import { OrderService } from "../../services/order/order.js";
import {
  checkMiddleware,
  checkRoleMiddleware,
  validateId,
  getUserMiddleware,
} from "../../middleware/base.js";
import {
  validateCreateOrderBody,
  validateUpdateOrderBody,
} from "../../middleware/odrer.js";
import { CONFIG } from "../../core/config.js";

export const orderRouter = Router();
const orderService = new OrderService();

orderRouter.use("/", (req, res, next) => {
  checkRoleMiddleware(req, res, next, CONFIG.ROLES.CUSTOMER);
});

orderRouter.use("/:id", (req, res, next) => {
  checkMiddleware(req, res, next, validateId);
});

orderRouter.use("/", (req, res, next) => {
  if (req.method == "POST")
    checkMiddleware(req, res, next, validateCreateOrderBody);
  else if (req.method == "PUT")
    checkMiddleware(req, res, next, validateUpdateOrderBody);
  else next();
});

orderRouter.get("/", async (req, res) => {
  const { id, role } = getUserMiddleware(req);
  if (!id || ![CONFIG.ROLES.EMPLOYEE, CONFIG.ROLES.ADMIN].includes(role))
    res.status(403).json("forbidden");
  else {
    const params = req.query;
    const status =
      typeof params.status == "string" &&
      Object.values(CONFIG.ORDER_STATUS).includes(Number(params.status))
        ? params.status
        : undefined;
    res.status(200).json(await orderService.getAllOrders(status));
  }
});

orderRouter.get("/:id", async (req, res) => {
  const { id, role } = getUserMiddleware(req);
  if (!id || !Object.values(CONFIG.ROLES).includes(role))
    res.status(403).json("forbidden");
  else {
    const order = await orderService.getOrderById(req.params.id);
    res.status(order ? 200 : 404).json(order ? order.toObject() : order);
  }
});

orderRouter.post("/", async (req, res) => {
  const { id, role } = getUserMiddleware(req);
  if (!id || role != CONFIG.ROLES.CUSTOMER) res.status(403).json("forbidden");
  else {
    const order = await orderService.createOrder(
      id,
      req.body,
      req.session.cart
    );
    const code = !order || typeof order == "string" ? 400 : 200;
    if (code != 400 && req.session) req.session.cart = [];
    res.status(code).json(code == 400 ? order : "order created");
  }
});

orderRouter.put("/:id", async (req, res) => {
  const { id, role } = getUserMiddleware(req);
  if (!id || !Object.values(CONFIG.ROLES).includes(role))
    res.status(403).json("forbidden");
  else {
    const order = await orderService.updateOrder(req.params.id, req.body);
    const code = !order || typeof order == "string" ? 400 : 200;
    res.status(code).json(order);
  }
});
