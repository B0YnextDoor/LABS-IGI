from app.app_models.bookModels import Book, BookGenre, Author


class BookRepository:
    @staticmethod
    def get_all(param: str):
        return Book.objects.order_by(f'-{param}')

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
