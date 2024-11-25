import { Router } from "express";
import { ReviewService } from "../../services/customer/review.js";
import {
  checkMiddleware,
  checkRoleMiddleware,
  getUserMiddleware,
  validateId,
} from "../../middleware/base.js";
import { CONFIG } from "../../core/config.js";
import { validateReviewBody } from "../../middleware/review.js";

export const reviewRouter = Router();
const reviewService = new ReviewService();

reviewRouter.use("/", (req, res, next) => {
  if (req.method != "GET")
    return checkRoleMiddleware(req, res, next, CONFIG.ROLES.CUSTOMER);
  next();
});

reviewRouter.use("/:id", (req, res, next) => {
  checkMiddleware(req, res, next, validateId);
});

reviewRouter.use("/", (req, res, next) => {
  if (!["PUT", "POST"].includes(req.method)) return next();
  checkMiddleware(req, res, next, validateReviewBody);
});

reviewRouter.get("/", async (_req, res) => {
  res.status(200).json(await reviewService.getAll());
});

reviewRouter.get("/:id", async (req, res) => {
  const review = await reviewService.getById(req.params.id);
  res.status(review ? 200 : 404).json(review);
});

reviewRouter.post("/", async (req, res) => {
  const { id, role } = getUserMiddleware(req);
  if (!id || role != CONFIG.ROLES.CUSTOMER)
    return res.status(403).json("forbidden");
  const result = await reviewService.create(req.body, id);
  const code = !result || typeof result === "string" ? 400 : 200;
  res.status(code).json(result);
});

reviewRouter.put("/:id", async (req, res) => {
  const { id, role } = getUserMiddleware(req);
  if (!id || role != CONFIG.ROLES.CUSTOMER)
    return res.status(403).json("forbidden");
  const result = await reviewService.update(req.params.id, req.body, id);
  const code = !result || typeof result === "string" ? 400 : 200;
  res.status(code).json(result);
});

reviewRouter.delete("/:id", async (req, res) => {
  const { id, role } = getUserMiddleware(req);
  if (!id || role != CONFIG.ROLES.CUSTOMER)
    return res.status(403).json("forbidden");
  const result = await reviewService.delete(req.params.id, id);
  const code = !result || typeof result === "string" ? 400 : 200;
  res.status(code).json(result);
});
