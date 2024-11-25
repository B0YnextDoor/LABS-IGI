import { Router } from "express";
import { NewsService } from "../../services/news/news.js";
import {
  checkMiddleware,
  checkRoleMiddleware,
  validateId,
} from "../../middleware/base.js";
import { CONFIG } from "../../core/config.js";
import { validateNewsBody } from "../../middleware/news.js";
import { createFileLoader } from "../../core/uploader.js";

export const newsRouter = Router();
const newsService = new NewsService();

const uploader = createFileLoader("news");

newsRouter.use("/", (req, res, next) => {
  if (req.method != "GET")
    return checkRoleMiddleware(req, res, next, CONFIG.ROLES.ADMIN);
  next();
});

newsRouter.use("/:id", (req, res, next) => {
  checkMiddleware(req, res, next, validateId);
});

newsRouter.get("/", async (_req, res) => {
  res.status(200).json(await newsService.getAll());
});

newsRouter.get("/:id", async (req, res) => {
  const news = await newsService.getById(req.params.id);
  res.status(news ? 200 : 404).json(news);
});

newsRouter.post(
  "/",
  uploader,
  (req, res, next) => {
    checkMiddleware(req, res, next, validateNewsBody);
  },
  async (req, res) => {
    const result = await newsService.create({
      ...req.body,
      imagePath: req.file?.path.replace(/\\/g, "/"),
    });
    res.status(result ? 200 : 400).json(result);
  }
);

newsRouter.put(
  "/:id",
  uploader,
  (req, res, next) => {
    checkMiddleware(req, res, next, validateNewsBody);
  },
  async (req, res) => {
    const result = await newsService.update(req.params.id, {
      ...req.body,
      imagePath: req.file?.path.replace(/\\/g, "/"),
    });
    const code = !result || typeof result === "string" ? 400 : 200;
    res.status(code).json(result);
  }
);

newsRouter.delete("/:id", async (req, res) => {
  const result = await newsService.delete(req.params.id);
  const code = !result || typeof result === "string" ? 400 : 200;
  res.status(code).json(result);
});
