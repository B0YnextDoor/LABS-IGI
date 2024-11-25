class Routes {
  HOME = "/";
  ACCOUNT = `${this.HOME}lk`;
  ORDERS = `${this.HOME}orders`;
  ORDER = this.ORDERS.slice(0, -1);
  CATALOG = `${this.HOME}books`;
  BOOK_FORM = this.CATALOG.slice(0, -1);
  AUTHOR = `${this.HOME}author`;
  GENRE = `${this.HOME}genre`;
  CART = `${this.HOME}cart`;
  ABOUT = `${this.HOME}about`;
  REVIEWS = `${this.HOME}reviews`;
  REVIEW = this.REVIEWS.slice(0, -1);
  NEWS = `${this.HOME}all-news`;
  NEWS_FORM = `${this.HOME}news`;
  EMPLOYEES = `${this.HOME}contacts`;
  EMPLOYEE_FORM = this.EMPLOYEES.slice(0, -1);
}

export const PAGES = new Routes();
