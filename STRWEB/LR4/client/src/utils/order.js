import { CONFIG } from "../config/config";

export const statusColors = ["yellow", "blue", "green", "red"];

export const statusText = [
  "Pending confirmation",
  "In delivery",
  "Delivered",
  "Cancelled",
];

export function getDefaultDate() {
  const now = new Date();
  const defaultDate = new Date(now);
  defaultDate.setDate(now.getDate() + 2);
  defaultDate.setHours(now.getHours() + CONFIG.GMT, 0, 0, 0);
  return defaultDate.toISOString().slice(0, 16);
}

export function validateDate(value) {
  const check = getDefaultDate();
  return value >= check || `Nearest delivery is ${check.toLocaleString()}`;
}

export function countPrice(items) {
  if (!items) return 0;
  return items.reduce((acc, v) => {
    return acc + v.amount * v.book.price;
  }, 0);
}

export function getBookIds(items) {
  return items.flatMap((item) => Array(item.amount).fill(item.book._id));
}

export function addToOrder(items, book_id, book_amount) {
  let isError = true;
  for (let item of items) {
    if (item.book._id === book_id && item.amount + 1 <= book_amount) {
      item.amount += 1;
      isError = false;
      break;
    }
  }
  return isError ? null : items;
}

export function removeFromOrder(items, book_id) {
  return items
    .map((item) => {
      if (item.book._id === book_id)
        return { ...item, amount: item.amount - 1 };
      return item;
    })
    .filter((item) => item.amount > 0);
}
