import { userApi } from "../api/api.js";

export const userService = {
  BASE_URL: "/user/",

  async profile(path) {
    if (["/sign-in", "/sign-up"].includes(path)) return;
    const response = await userApi.get(`${this.BASE_URL}profile`);
    if (response.status == 200) return response.data;
  },

  async orders() {
    const response = await userApi.get(`${this.BASE_URL}orders`);
    if (response.status == 200) return response.data;
  },

  async update(data) {
    const response = await userApi.put(`${this.BASE_URL}update`, data);
    return response;
  },
};
