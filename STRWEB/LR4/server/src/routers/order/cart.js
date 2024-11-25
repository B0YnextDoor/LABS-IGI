import { Router } from "express";
import {
  checkMiddleware,
  checkRoleMiddleware,
  getUserMiddleware,
  validateId,
} from "../../middleware/base.js";
import { CartService } from "../../services/order/cart.js";
import { CONFIG } from "../../core/config.js";

export const cartRouter = Router();
const cartService = new CartService();

cartRouter.use("/", (req, res, next) => {
  const { id, role } = getUserMiddleware(req);
  if (!id || role != CONFIG.ROLES.CUSTOMER)
    return res.status(403).json("forbidden");
  return next();
});

cartRouter.use("/:id", (req, res, next) => {
  checkMiddleware(req, res, next, validateId);
});

cartRouter.get("/", async (req, res) => {
  res.status(200).json(await cartService.getCart(req.session.cart));
});

cartRouter.put("/:id", async (req, res) => {
  const bookId = req.params.id;
  const result = await cartService.addBook(bookId, req.session.cart);
  if (typeof result == "string")
    res.status(400).json(result || "Can't add the book!");
  else {
    req.session.cart.push(bookId);
    res.status(200).json("Book added");
  }
});

cartRouter.delete("/:id", async (req, res) => {
  const result = await cartService.removeBook(req.params.id, req.session.cart);
  if (typeof result == "string")
    res.status(400).json(result || "Can't delete the book!");
  else {
    req.session.cart = result;
    res.status(200).json("Book deleted");
  }
});
