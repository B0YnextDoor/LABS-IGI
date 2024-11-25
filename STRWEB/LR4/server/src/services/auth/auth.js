import { CONFIG } from "../../core/config.js";
import { comparePassword } from "../../core/security.js";
import { destroySession } from "../../core/session.js";
import { CustomerService } from "../customer/customer.js";
import { EmployeeService } from "../employee/employee.js";
import { TokenService } from "./token.js";

export class AuthService {
  customerService = new CustomerService();
  employeeService = new EmployeeService();
  tokenService = new TokenService();
  loginError = "Log In error";
  regError = "Registration error";
  wrongCreds = "Wrong email or password!";

  setCookies(res, tokens) {
    this.tokenService.setCookies(res, tokens);
  }

  async signInUser(user) {
    const db_customer = await this.customerService.getByEmail(user.email);
    if (!db_customer) return this.signInEmployee(user);
    if (!(await comparePassword(user.password, db_customer.password)))
      return this.wrongCreds;
    const tokens = this.tokenService.genetateTokens({
      id: db_customer._id,
      role: CONFIG.ROLES.CUSTOMER,
    });
    return tokens ? tokens : this.loginError;
  }

  async signInEmployee(user) {
    const db_employee = await this.employeeService.getByEmail(user.email);
    if (
      !db_employee ||
      !(await comparePassword(user.password, db_employee.password))
    )
      return this.wrongCreds;
    const tokens = this.tokenService.genetateTokens({
      id: db_employee._id,
      role: db_employee.isAdmin ? CONFIG.ROLES.ADMIN : CONFIG.ROLES.EMPLOYEE,
    });
    return tokens ? tokens : this.loginError;
  }

  async authWithAccount(user) {
    const db_user = await this.customerService.getByEmail(user.email);
    if (!db_user) return this.signUpCustomer(user);
    const tokens = this.tokenService.genetateTokens({
      id: db_user._id,
      role: CONFIG.ROLES.CUSTOMER,
    });
    return tokens ? tokens : this.loginError;
  }

  async signUp(user) {
    const new_user = await this.customerService.create(user);
    const isError = typeof new_user == "string";
    if (!new_user || isError) return isError ? new_user : this.regError;
    const tokens = this.tokenService.genetateTokens({
      id: new_user._id,
      role: CONFIG.ROLES.CUSTOMER,
    });
    return tokens ? tokens : this.regError;
  }

  async logOut(req, res) {
    if (req.session)
      return await destroySession(req, res, this.tokenService.removeCookies);
    else {
      this.tokenService.removeCookies(res);
      return res.status(200).json("logout");
    }
  }
}
