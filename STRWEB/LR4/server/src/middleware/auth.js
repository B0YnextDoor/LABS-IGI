import { CONFIG } from "../core/config.js";
import { TokenService } from "../services/auth/token.js";

const tokenService = new TokenService();

export async function checkIsAuth(req, res, next) {
  if (req.cookies[`${CONFIG.ACCESS_TOKEN}`])
    return res.redirect(req.get("Referrer") || "/");
  next();
}

export function getUserData(req) {
  const userData = tokenService.verifyToken(
    req.cookies[`${CONFIG.ACCESS_TOKEN}`]
  );
  return !userData || typeof userData == "string" ? {} : userData;
}

export function checkUserRole(req, role) {
  const userData = getUserData(req);
  return Boolean(
    userData && userData.hasOwnProperty("role") && userData.role >= role
  );
}

export async function verifyUser(req, res, next) {
  const accessToken = tokenService.verifyToken(
    req.cookies[`${CONFIG.ACCESS_TOKEN}`]
  );
  if (accessToken) return next();
  const tokens = await tokenService.refreshTokens(
    req.cookies[`${CONFIG.REFRESH_TOKEN}`]
  );
  if (!tokens) {
    tokenService.removeCookies(res);
  } else {
    console.log(req.cookies);
    tokenService.setCookies(res, tokens);
    req.cookies[`${CONFIG.ACCESS_TOKEN}`] = tokens.accessToken;
    req.cookies[`${CONFIG.REFRESH_TOKEN}`] = tokens.refreshToken;
    console.log("refresh");
  }
  return next();
}
