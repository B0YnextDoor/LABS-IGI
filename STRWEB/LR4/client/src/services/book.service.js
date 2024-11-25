import { userApi } from "../api/api";

export const bookService = {
  BASE_URL: "/books/",

  async getCatalog() {
    const response = await userApi.get(`${this.BASE_URL}?title=all`);
    if (response.status == 200) return response.data;
  },

  async getAll(title, order, page, isLoading) {
    if (isLoading) return;
    const response = await userApi.get(
      `${this.BASE_URL}?page=${page || 1}${title ? `&title=${title}` : ""}${
        order ? `&order=${order}` : ""
      }`
    );
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

  async getAuthors() {
    const response = await userApi.get("/authors/");
    if (response.status == 200) return response.data;
  },

  async getGenres() {
    const response = await userApi.get("/genres/");
    if (response.status == 200) return response.data;
  },
};
