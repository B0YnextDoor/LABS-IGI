import jwt from "jsonwebtoken";
const { sign, verify } = jwt;
import { CustomerService } from "../customer/customer.js";
import { EmployeeService } from "../employee/employee.js";
import { CONFIG } from "../../core/config.js";

const accessCookieOptions = {
  domain: CONFIG.COOKIE_DOMAIN,
  sameSite: CONFIG.COOKIE_SAME_SITE,
};

const refreshCookieOptions = {
  domain: CONFIG.COOKIE_DOMAIN,
  sameSite: CONFIG.COOKIE_SAME_SITE,
  httpOnly: true,
};

export class TokenService {
  customerService = new CustomerService();
  employeeService = new EmployeeService();

  genetateTokens(data) {
    try {
      const accessToken = sign(data, CONFIG.ACCESS_SECRET, {
        expiresIn: `${CONFIG.ACCESS_EXPIRES_IN}m`,
      });
      const refreshToken = sign(data, CONFIG.REFRESH_SECRET, {
        expiresIn: `${CONFIG.REFRESH_EXPIRES_IN}m`,
      });
      return { accessToken, refreshToken };
    } catch (e) {
      console.error(e);
      return null;
    }
  }

  verifyToken(token, type = false) {
    try {
      if (!token) return null;
      const data = verify(
        token,
        !type ? CONFIG.ACCESS_SECRET : CONFIG.REFRESH_SECRET
      );
      return data;
    } catch (e) {
      return null;
    }
  }

  async refreshTokens(refreshToken) {
    if (!refreshToken) return null;
    const userData = this.verifyToken(refreshToken, true);
    if (!userData || typeof userData == "string") return null;
    const user =
      userData.role == CONFIG.ROLES.CUSTOMER
        ? await this.customerService.getById(userData.id)
        : await this.employeeService.getById(userData.id);
    if (!user) return null;
    return this.genetateTokens({
      id: user._id,
      role:
        typeof user.isAdmin === "undefined"
          ? CONFIG.ROLES.CUSTOMER
          : user.isAdmin
          ? CONFIG.ROLES.ADMIN
          : CONFIG.ROLES.EMPLOYEE,
    });
  }

  setCookies(res, tokens) {
    const now = new Date();
    res.cookie(CONFIG.ACCESS_TOKEN, tokens.accessToken, {
      ...accessCookieOptions,
      expires: new Date(now.getTime() + CONFIG.ACCESS_EXPIRES_IN * 60000),
    });
    res.cookie(CONFIG.REFRESH_TOKEN, tokens.refreshToken, {
      ...refreshCookieOptions,
      expires: new Date(now.getTime() + CONFIG.REFRESH_EXPIRES_IN * 60000),
    });
  }

  removeCookies(res) {
    res.clearCookie(CONFIG.ACCESS_TOKEN, accessCookieOptions);
    res.clearCookie(CONFIG.REFRESH_TOKEN, refreshCookieOptions);
  }
}
