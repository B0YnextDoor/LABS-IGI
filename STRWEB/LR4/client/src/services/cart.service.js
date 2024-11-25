import { userApi } from "../api/api";

export const cartService = {
  BASE_URL: "/cart/",

  async get() {
    const response = await userApi.get(this.BASE_URL);
    if (response.status == 200) return response.data;
  },

  async add(id) {
    if (!id) return;
    const response = await userApi.put(`${this.BASE_URL}${id}`);
    return response;
  },

  async delete(id) {
    if (!id) return;
    const response = await userApi.delete(`${this.BASE_URL}${id}`);
    return response;
  },
};
