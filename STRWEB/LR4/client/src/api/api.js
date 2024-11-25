import axios from "axios";
import { CONFIG } from "../config/config";

const options = {
  baseURL: CONFIG.BASE_URL,
  headers: {
    "Content-Type": "application/json",
  },
  withCredentials: true,
};

export const FORM_OPTIONS = {
  ...options,
  headers: {
    "Content-Type": "multipart/form-data",
  },
};

export const userApi = axios.create(options);
