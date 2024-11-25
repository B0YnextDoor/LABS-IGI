import { config } from "dotenv";

config();

class Config {
  DB_PORT = String(process.env.PORT || 1337);
  DB_URL = String(
    process.env.DATABASE_URL || "mongodb://localhost:27017/bookshop"
  );

  SALT_ROUNDS = Number(process.env.SALT_ROUNDS) ?? 10;

  COOKIE_DOMAIN = String(process.env.COOKIE_DOMAIN || "localhost");
  COOKIE_SAME_SITE = String(process.env.COOKIE_SAME_SITE || "lax");

  REDIS_URL = String(process.env.REDIS_URL || "redis://@localhost:6379");
  SESSION_ID = String(process.env.SESSION_ID || "session-id");
  SESSION_SECRET = String(process.env.SESSION_SECRET || "secret-session");
  SESSION_MAX_AGE = 1000 * 60 * 60 * Number(process.env.SESSION_MAX_AGE ?? 24);

  ACCESS_TOKEN = String(process.env.ACCESS_TOKEN || "access-token");
  REFRESH_TOKEN = String(process.env.REFRESH_TOKEN || "refresh-token");
  ACCESS_SECRET = String(process.env.JWT_ACCESS_SECRET || "jwt-access-secret");
  REFRESH_SECRET = String(
    process.env.JWT_REFRESH_SECRET || "jwt-refresh-secret"
  );
  ACCESS_EXPIRES_IN = Number(process.env.ACCESS_TOKEN_EXPIRES_IN || 15);
  REFRESH_EXPIRES_IN = Number(process.env.REFRESH_TOKEN_EXPIRES_IN || 60);

  CORS_POLICY = String(process.env.CORS_POLICY || "same-origin");
  CORS_ORIGIN = String(process.env.CORS_ORIGIN || "*");

  REDIRECT_URL = String(process.env.CORS_ORIGIN || "http://localhost:5173/");

  GOOGLE_CLIENT_ID = String(process.env.GOOGLE_CLIENT_ID);
  GOOGLE_CLIENT_SECRET = String(process.env.GOOGLE_CLIENT_SECRET);
  GOOGLE_CALLBACK = String(
    process.env.GOOGLE_CALLBACK || "/auth/google/callback"
  );

  FACEBOOK_CLIENT_ID = String(process.env.FACEBOOK_CLIENT_ID);
  FACEBOOK_CLIENT_SECRET = String(process.env.FACEBOOK_CLIENT_SECRET);
  FACEBOOK_CALLBACK = String(
    process.env.FACEBOOK_CALLBACK || "/auth/facebook/callback"
  );

  ROLES = {
    CUSTOMER: 1,
    EMPLOYEE: 2,
    ADMIN: 3,
  };

  ORDER_STATUS = {
    PENDING: 1,
    ACTIVE: 2,
    DELIVERED: 3,
    CANCELED: 4,
  };
}

export const CONFIG = new Config();
