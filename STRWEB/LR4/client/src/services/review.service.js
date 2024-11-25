import { userApi } from "../api/api.js";

export const reviewService = {
  BASE_URL: "/reviews/",

  async getAll() {
    const response = await userApi.get(this.BASE_URL);
    if (response.status == 200) return response.data;
  },

  async getById(id) {
    if (!id) return;
    const response = await userApi.get(`${this.BASE_URL}${id}`);
    if (response.status == 200) return response.data;
  },

  async create(data) {
    const response = await userApi.post(this.BASE_URL, data);
    return response;
  },

  async update(id, data) {
    if (!id) return;
    const response = await userApi.put(`${this.BASE_URL}${id}`, data);
    return response;
  },

  async delete(id) {
    if (!id) return;
    const response = await userApi.delete(`${this.BASE_URL}${id}`);
    return response;
  },
};
