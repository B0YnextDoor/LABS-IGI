import helmet from "helmet";
import cors from "cors";
import { authorRouter } from "./book/author.js";
import { genreRouter } from "./book/genre.js";
import { bookRouter } from "./book/book.js";
import { authRouter } from "./auth/auth.js";
import { cartRouter } from "./order/cart.js";
import { orderRouter } from "./order/order.js";
import { userRouter } from "./user/user.js";
import { reviewRouter } from "./review/review.js";
import { newsRouter } from "./news/news.js";
import { employeeRouter } from "./user/employee.js";
import { CONFIG } from "../core/config.js";
import {
  checkAuthMiddleware,
  checkSessionMiddleware,
} from "../middleware/base.js";

function getCORSPolicy() {
  const policy = CONFIG.CORS_POLICY;
  return !policy
    ? undefined
    : policy == "same-site"
    ? "same-site"
    : policy == "same-origin"
    ? "same-origin"
    : "cross-origin";
}

export function setupCORS(app) {
  const corsOrigin = CONFIG.CORS_ORIGIN;
  const corsPolicy = getCORSPolicy();
  app.use(
    cors({
      origin: corsOrigin,
      credentials: true,
    })
  );
  app.use(helmet({ crossOriginResourcePolicy: { policy: corsPolicy } }));
}

export function setupRoutes(app) {
  app.use("/", checkAuthMiddleware);
  app.use("/", checkSessionMiddleware);

  app.use("/auth", authRouter);
  app.use("/user", userRouter);
  app.use("/authors", authorRouter);
  app.use("/genres", genreRouter);
  app.use("/books", bookRouter);
  app.use("/cart", cartRouter);
  app.use("/orders", orderRouter);
  app.use("/reviews", reviewRouter);
  app.use("/news", newsRouter);
  app.use("/employees", employeeRouter);
}
