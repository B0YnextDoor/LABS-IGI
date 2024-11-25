import { createClient } from "redis";
import RedisStore from "connect-redis";
import session from "express-session";
import { CONFIG } from "./config.js";

const sessionCookieOptions = {
  httpOnly: true,
  maxAge: CONFIG.SESSION_MAX_AGE,
  sameSite: CONFIG.COOKIE_SAME_SITE,
  domain: CONFIG.COOKIE_DOMAIN,
};

export async function setupSession(app) {
  const client = createClient({
    url: CONFIG.REDIS_URL,
  });

  client.on("error", function (err) {
    console.log("Could not establish a connection with redis.\n" + err);
    process.exit(1);
  });

  client.on("connect", function (_) {
    console.log("Connected to redis successfully!");
  });

  const redisStore = new RedisStore({
    client: client,
    prefix: "cart:",
  });

  try {
    await client.connect();
    app.use(
      session({
        store: redisStore,
        secret: CONFIG.SESSION_SECRET,
        resave: false,
        saveUninitialized: true,
        cookie: sessionCookieOptions,
        name: CONFIG.SESSION_ID,
      })
    );
  } catch (error) {
    console.error("Failed to setup session:", error);
    throw error;
  }
}

export const destroySession = async (req, res, cb) =>
  await req.session.destroy((err) => {
    if (err) {
      console.log(`Session destroying error: ${err}`);
      return res.status(500).json("Server error!");
    }
    const { maxAge, ...rest } = sessionCookieOptions;
    res.clearCookie(CONFIG.SESSION_ID, rest);
    cb(res);
    return res.status(200).json("logout");
  });
