import { userApi, FORM_OPTIONS } from "../api/api";
import axios from "axios";

export const employeeService = {
  BASE_URL: "/employees/",

  async getAll(filter, order, page, isLoading) {
    if (isLoading) return;
    const response = await userApi.get(
      `${this.BASE_URL}?page=${page || 1}${filter ? `&filter=${filter}` : ""}${
        order ? `&order=${order}` : ""
      }`
    );
    if (response.status === 200) return response.data;
  },

  async getById(id) {
    if (!id) return;
    const response = await userApi.get(`${this.BASE_URL}${id}`);
    if (response.status === 200) return response.data;
  },

  async create(data) {
    const response = await axios.post(this.BASE_URL, data, FORM_OPTIONS);
    return response;
  },

  async update(id, data) {
    if (!id) return;
    const response = await axios.put(
      `${this.BASE_URL}${id}`,
      data,
      FORM_OPTIONS
    );
    return response;
  },

  async delete(id) {
    if (!id) return;
    const response = await userApi.delete(`${this.BASE_URL}${id}`);
    return response;
  },
};
