from app.services.bookService import BookService
from collections import Counter


class CartService:
    @staticmethod
    def form_cart(cart):
        book_count = Counter(cart)
        books = []
        for id, count in book_count.items():
            book = BookService.get_by_id(id)
            if book is not None:
                books.append(
                    {'id': book.id, 'title': book.title, 'author': book.author,
                     'genre': book.genre, 'price': book.price * count, 'ammount': count})
        return books

    @staticmethod
    def reform_cart(cart: list):
        cart.sort()
        books = []
        for id in cart:
            book = BookService.get_by_id(id)
            if book is not None:
                books.append(book)
        return books

    @staticmethod
    def count_book(cart: list, book_id: int):
        book = BookService.get_by_id(book_id)
        book_amount = Counter(cart).get(book_id)
        return cart if book_amount is None or book.amount >= book_amount + 1 else None
