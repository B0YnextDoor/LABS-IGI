import { Router } from "express";
import { GenreService } from "../../services/book/genre.js";
import {
  validateId,
  checkMiddleware,
  checkRoleMiddleware,
} from "../../middleware/base.js";
import { validateGenreBody } from "../../middleware/book.js";
import { CONFIG } from "../../core/config.js";

export const genreRouter = Router();
const genreService = new GenreService();

genreRouter.use("/", (req, res, next) => {
  if (req.method != "GET" || /.+/.test(req.path)) {
    return checkRoleMiddleware(req, res, next, CONFIG.ROLES.ADMIN);
  }
  next();
});

genreRouter.use("/:id", (req, res, next) => {
  checkMiddleware(req, res, next, validateId);
});

genreRouter.use("/", (req, res, next) => {
  if (!["PUT", "POST"].includes(req.method)) return next();
  checkMiddleware(req, res, next, validateGenreBody);
});

genreRouter.get("/", async (_req, res) => {
  res.status(200).json(await genreService.getAll());
});

genreRouter.get("/:id", async (req, res) => {
  const genre = await genreService.getById(req.params.id);
  res.status(genre ? 200 : 404).json(genre);
});

genreRouter.post("/", async (req, res) => {
  const result = await genreService.create(req.body);
  res.status(result ? 200 : 400).json(result);
});

genreRouter.put("/:id", async (req, res) => {
  const result = await genreService.update(req.params.id, req.body);
  const code = !result ? 400 : typeof result === "string" ? 404 : 200;
  res.status(code).json(result);
});

genreRouter.delete("/:id", async (req, res) => {
  const result = await genreService.delete(req.params.id);
  const code = !result ? 400 : typeof result === "string" ? 404 : 200;
  res.status(code).json(result);
});
