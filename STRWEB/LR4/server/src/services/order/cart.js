import { BookService } from "../book/book.js";

export class CartService {
  bookService = new BookService();

  formCart(cart) {
    return cart
      ? cart.reduce((acc, curr) => {
          acc[curr] = (acc[curr] || 0) + 1;
          return acc;
        }, {})
      : {};
  }

  async getCart(cart) {
    if (!cart) return [];
    const formedCart = this.formCart(cart);
    return await Promise.all(
      Object.entries(formedCart).map(async ([bookId, amount]) => ({
        amount: amount,
        book: await this.bookService.getById(bookId),
      }))
    );
  }

  async checkBook(id) {
    const book = await this.bookService.getById(id);
    return book ? book : "Book doesn't exist";
  }

  async addBook(id, cart) {
    const book = await this.checkBook(id);
    if (typeof book == "string") return book;
    const formedCart = this.formCart(cart);
    if (
      book.amount == 0 ||
      (Object.keys(formedCart).length > 0 && book.amount < formedCart[id] + 1)
    )
      return "Not enough books in catalog!";
    return book;
  }

  async removeBook(id, cart) {
    if (!cart || !cart.length) return "Cart is empty!";
    const book = await this.checkBook(id);
    if (typeof book === "string") return book;
    if (!cart.includes(id)) return "Book is not in the cart!";
    cart.sort();
    cart.splice(cart.indexOf(id), 1);
    return cart;
  }
}
