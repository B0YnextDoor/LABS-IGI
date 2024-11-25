import { Router } from "express";
import { EmployeeService } from "../../services/employee/employee.js";
import { createFileLoader } from "../../core/uploader.js";
import {
  checkMiddleware,
  checkRoleMiddleware,
  validateId,
} from "../../middleware/base.js";
import { validateUserBody, validateInfoBody } from "../../middleware/user.js";
import { CONFIG } from "../../core/config.js";

export const employeeRouter = Router();
const employeeService = new EmployeeService();

const uploader = createFileLoader("employees");

employeeRouter.use("/", (req, res, next) => {
  if (req.method != "GET")
    return checkRoleMiddleware(req, res, next, CONFIG.ROLES.ADMIN);
  next();
});

employeeRouter.use("/:id", (req, res, next) => {
  checkMiddleware(req, res, next, validateId);
});

employeeRouter.get("/", async (req, res) => {
  const params = req.query;
  res
    .status(200)
    .json(
      await employeeService.getInfo(params.filter, params.order, params.page)
    );
});

employeeRouter.get("/:id", async (req, res) => {
  const emp = await employeeService.getById(req.params.id);
  res.status(emp ? 200 : 404).json(emp);
});

employeeRouter.post(
  "/",
  uploader,
  (req, res, next) => {
    checkMiddleware(req, res, next, validateUserBody);
  },
  (req, res, next) => {
    checkMiddleware(req, res, next, validateInfoBody);
  },
  async (req, res) => {
    const result = await employeeService.create({
      ...req.body,
      imagePath: req.file?.path.replace(/\\/g, "/"),
    });
    const code = !result || typeof result === "string" ? 400 : 200;
    res.status(code).json(result);
  }
);

employeeRouter.put("/:id", uploader, async (req, res) => {
  const result = await employeeService.update(req.params.id, {
    ...req.body,
    imagePath: req.file?.path.replace(/\\/g, "/"),
  });
  const code = !result || typeof result === "string" ? 400 : 200;
  res.status(code).json(result);
});

employeeRouter.delete("/:id", async (req, res) => {
  const result = await employeeService.delete(req.params.id);
  const code = !result || typeof result === "string" ? 400 : 200;
  res.status(code).json(result);
});
