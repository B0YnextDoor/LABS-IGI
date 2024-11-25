import express from "express";
import cookieParser from "cookie-parser";
import { setupCORS, setupRoutes } from "./src/routers/routers.js";
import { setupSession } from "./src/core/session.js";
import path from "path";
import mongoose from "mongoose";
import { fileURLToPath } from "url";
import { dirname } from "path";
import passport from "./src/core/passport-config.js";
import { CONFIG } from "./src/core/config.js";

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);

const app = express();

async function main() {
  setupCORS(app);
  app.use(cookieParser());
  await setupSession(app);
  app.use(express.json());
  app.use(passport.initialize());
  app.use("/src/static", express.static(path.join(__dirname, "src/static")));
  setupRoutes(app);

  app.get("/", (req, res) => {
    console.log(req.session);
    res.status(200).json("service is working");
  });

  app.all("*", (_req, res) => {
    res.status(404).json({ message: "Not found" });
  });

  const port = CONFIG.DB_PORT;
  app.listen(port, () => {
    console.log(`Server is running on port ${port}`);
  });
}

main()
  .then(async () => {
    await mongoose.connect(CONFIG.DB_URL);
  })
  .catch(async (e) => {
    console.error(e);
    await mongoose.disconnect();
    process.exit(1);
  });
