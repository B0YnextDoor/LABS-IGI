import { hash, compare } from "bcrypt";
import { CONFIG } from "./config.js";

export async function hashPassword(password) {
  return await hash(password, Number(CONFIG.SALT_ROUNDS));
}

export async function comparePassword(password, dbPassword) {
  return await compare(password, dbPassword);
}
