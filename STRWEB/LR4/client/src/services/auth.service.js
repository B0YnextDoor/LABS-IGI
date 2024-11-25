import { userApi } from "../api/api.js";

export const authService = {
  BASE_URL: "/auth/",

  async auth(data, type) {
    const response = await userApi.post(
      `${this.BASE_URL}sign-${type ? "in" : "up"}`,
      data
    );
    return response;
  },

  async authAccount(type) {
    const response = await userApi.get(
      `${this.BASE_URL}${type ? "google" : "facebook"}`
    );
    return response;
  },

  async logOut() {
    const response = await userApi.post(`${this.BASE_URL}log-out`);
    return response;
  },
};
