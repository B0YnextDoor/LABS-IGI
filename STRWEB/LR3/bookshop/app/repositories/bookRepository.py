from app.app_models.bookModels import Book, BookGenre, Author

limit = 3


class BookRepository:
    @staticmethod
    def get_all_admin():
        return Book.objects.all()

    @staticmethod
    def get_all(title: str | None, param: str | None, page: int | None):
        books = Book.objects.all() if title is None else Book.objects.filter(
            title__contains=title)
        total = len(books)
        if param is None or param != 'price':
            param = 'amount'
        if page is None or page*3 > total:
            page = 0
        offset = page*limit
        return books.order_by(f'-{param}')[offset:offset+limit], total

    @staticmethod
    def get_by_id(id: int):
        return Book.objects.filter(id=id).first()

    @staticmethod
    def create(title: str, price: float, amount: int, genre: int, author: int):
        try:
            book_genre = BookGenre.objects.get(id=genre)
            book_author = Author.objects.get(id=author)
            book = Book(title=title, price=price, amount=amount,
                        genre=book_genre, author=book_author)
            book.save()
            return book
        except:
            return None

    @staticmethod
    def update(id: int, title: str, price: float, amount: int, genre: int, author: int):
        try:
            book = BookRepository.get_by_id(id)
            book.title = title
            book.price = price
            book.amount = amount
            book.genre = BookGenre.objects.get(id=genre)
            book.author = Author.objects.get(id=author)
            book.save()
            return book
        except:
            return None

    @staticmethod
    def delete(id: int):
        try:
            book = BookRepository.get_by_id(id)
            if book is None:
                return None
            book.delete()
        except:
            return None
