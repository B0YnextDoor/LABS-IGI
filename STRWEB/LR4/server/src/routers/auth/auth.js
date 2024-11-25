import { Router } from "express";
import { checkIsAuth } from "../../middleware/auth.js";
import passport from "../../core/passport-config.js";
import { AuthService } from "../../services/auth/auth.js";
import { checkMiddleware } from "../../middleware/base.js";
import { validateUserBody, validateInfoBody } from "../../middleware/user.js";
import { CONFIG } from "../../core/config.js";

export const authRouter = Router();
const authService = new AuthService();

authRouter.use("/", (req, res, next) => {
  if (req.path == "/log-out") return next();
  checkIsAuth(req, res, next);
});

authRouter.use("/", (req, res, next) => {
  if (req.path == "/log-out" || req.method == "GET") return next();
  checkMiddleware(req, res, next, validateUserBody);
});

authRouter.use("/sign-up", (req, res, next) => {
  checkMiddleware(req, res, next, validateInfoBody);
});

authRouter.post(
  "/sign-in",
  (req, res, next) => {
    passport.authenticate("local", { session: false }, (err, user, info) => {
      if (err) {
        return res.status(500).json({ message: "Internal server error" });
      }
      if (!user) {
        return res
          .status(401)
          .json({ message: info ? info.message : "Unauthorized" });
      }
      req.user = user;
      next();
    })(req, res, next);
  },
  async (req, res) => {
    authService.setCookies(res, req.user);
    res.status(200).json("successfull login");
  }
);

authRouter.get("/google", passport.authenticate("google", { session: false }));

authRouter.get(
  "/google/callback",
  (req, res, next) => {
    passport.authenticate("google", { session: false }, (err, user, info) => {
      if (err) {
        return res.status(500).json({ message: "Internal server error" });
      }
      if (!user) {
        return res
          .status(401)
          .json({ message: info ? info.message : "Unauthorized" });
      }
      req.user = user;
      next();
    })(req, res, next);
  },
  async (req, res) => {
    authService.setCookies(res, req.user);
    res.redirect(CONFIG.REDIRECT_URL);
  }
);

authRouter.get(
  "/facebook",
  passport.authenticate("facebook", { session: false })
);

authRouter.get(
  "/facebook/callback",
  (req, res, next) => {
    passport.authenticate("facebook", { session: false }, (err, user, info) => {
      if (err) {
        return res.status(500).json({ message: "Internal server error" });
      }
      if (!user) {
        return res
          .status(401)
          .json({ message: info ? info.message : "Unauthorized" });
      }
      req.user = user;
      next();
    })(req, res, next);
  },
  async (req, res) => {
    authService.setCookies(res, req.user);
    res.redirect(CONFIG.REDIRECT_URL);
  }
);

authRouter.post("/sign-up", async (req, res) => {
  const result = await authService.signUp(req.body);
  if (typeof result == "string") res.status(401).json(result);
  else {
    authService.setCookies(res, result);
    res.status(200).json("successfull login");
  }
});

authRouter.post(
  "/log-out",
  async (req, res) => await authService.logOut(req, res)
);
