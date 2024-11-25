import { validationResult } from "express-validator";
import { isValidObjectId } from "mongoose";
import { verifyUser, getUserData, checkUserRole } from "./auth.js";
import { CONFIG } from "../core/config.js";

export const validateId = (req) => {
  const id = req.params.id;
  if (!id || !isValidObjectId(id)) return "Invalid ObjectId!";
  return "";
};

export const checkMiddleware = async (req, res, next, cb) => {
  try {
    const message = await cb(req);
    const errors = validationResult(req);
    if (typeof message === "string" && message.length) {
      return res.status(400).json(message);
    } else if (!errors.isEmpty()) {
      console.log(errors);
      return res.status(400).json(errors.errors[0].msg);
    }
    next();
  } catch (error) {
    next(error);
  }
};

export const checkAuthMiddleware = async (req, res, next) => {
  if (req.path == "/" || req.path.includes("/auth/")) return next();
  await verifyUser(req, res, next);
};

export const getUserMiddleware = (req) => getUserData(req);

export const checkRoleMiddleware = (req, res, next, role) => {
  if (checkUserRole(req, role)) return next();
  return res.status(403).json("Not enough privelege level!");
};

export const checkSessionMiddleware = (req, _, next) => {
  if (req.path.includes("auth")) return next();
  const userData = getUserMiddleware(req);
  if (
    userData.id &&
    userData.role == CONFIG.ROLES.CUSTOMER &&
    !req.session.cart
  ) {
    req.session.cart = new Array();
  }
  req.session.save();
  next();
};
