import { Router } from "express";
import { AuthorService } from "../../services/book/author.js";
import {
  checkMiddleware,
  validateId,
  checkRoleMiddleware,
} from "../../middleware/base.js";
import { validateAuthorBody } from "../../middleware/book.js";
import { CONFIG } from "../../core/config.js";

export const authorRouter = Router();
const authorService = new AuthorService();

authorRouter.use("/", (req, res, next) => {
  if (req.method != "GET" || /.+/.test(req.path))
    return checkRoleMiddleware(req, res, next, CONFIG.ROLES.ADMIN);
  next();
});

authorRouter.use("/:id", (req, res, next) => {
  checkMiddleware(req, res, next, validateId);
});

authorRouter.use("/", (req, res, next) => {
  if (!["PUT", "POST"].includes(req.method)) return next();
  checkMiddleware(req, res, next, validateAuthorBody);
});

authorRouter.get("/", async (_req, res) => {
  res.status(200).json(await authorService.getAll());
});

authorRouter.get("/:id", async (req, res) => {
  const author = await authorService.getById(req.params.id);
  res.status(author ? 200 : 404).json(author);
});

authorRouter.post("/", async (req, res) => {
  const result = await authorService.create(req.body);
  res.status(result ? 200 : 400).json(result);
});

authorRouter.put("/:id", async (req, res) => {
  const result = await authorService.update(req.params.id, req.body);
  const code = !result ? 400 : typeof result === "string" ? 404 : 200;
  res.status(code).json(result);
});

authorRouter.delete("/:id", async (req, res) => {
  const result = await authorService.delete(req.params.id);
  const code = !result ? 400 : typeof result === "string" ? 404 : 200;
  res.status(code).json(result);
});
