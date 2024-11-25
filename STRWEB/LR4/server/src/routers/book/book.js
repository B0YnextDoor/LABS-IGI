import { Router } from "express";
import { BookService } from "../../services/book/book.js";
import {
  checkMiddleware,
  validateId,
  checkRoleMiddleware,
} from "../../middleware/base.js";
import { validateBookBody } from "../../middleware/book.js";
import { CONFIG } from "../../core/config.js";

export const bookRouter = Router();
const bookService = new BookService();

bookRouter.use("/", (req, res, next) => {
  if (req.method != "GET")
    return checkRoleMiddleware(req, res, next, CONFIG.ROLES.ADMIN);
  return /\.+/.test(req.path)
    ? checkRoleMiddleware(req, res, next, CONFIG.ROLES.CUSTOMER)
    : next();
});

bookRouter.use("/:id", (req, res, next) => {
  checkMiddleware(req, res, next, validateId);
});

bookRouter.use("/", (req, res, next) => {
  if (!["PUT", "POST"].includes(req.method)) return next();
  checkMiddleware(req, res, next, validateBookBody);
});

bookRouter.get("/", async (req, res) => {
  const params = req.query;
  res
    .status(200)
    .json(await bookService.getAll(params.title, params.order, params.page));
});

bookRouter.get("/:id", async (req, res) => {
  const book = await bookService.getById(req.params.id);
  res.status(book ? 200 : 404).json(book);
});

bookRouter.post("/", async (req, res) => {
  const result = await bookService.create(req.body);
  const code = !result || typeof result === "string" ? 400 : 200;
  res.status(code).json(result);
});

bookRouter.put("/:id", async (req, res) => {
  const result = await bookService.update(req.params.id, req.body);
  const code = !result ? 400 : typeof result === "string" ? 404 : 200;
  res.status(code).json(result);
});

bookRouter.delete("/:id", async (req, res) => {
  const result = await bookService.delete(req.params.id);
  const code = !result ? 400 : typeof result === "string" ? 404 : 200;
  res.status(code).json(result);
});
