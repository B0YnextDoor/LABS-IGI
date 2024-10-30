from app.repositories.bookRepository import BookRepository


class BookService:
    @staticmethod
    def get_all_admin():
        return BookRepository.get_all_admin()

    @staticmethod
    def get_all(title: str | None, param: str | None, page: int | None):
        result = dict()
        if page is not None:
            page = int(page)
        books, total = BookRepository.get_all(title, param, page)
        result['total'] = total
        result['books'] = list()
        for book in books:
            result['books'].append({
                'id': book.id,
                'title': book.title,
                'price': book.price,
                'amount': book.amount,
                'author_surname': book.author.surname,
                'author_name': book.author.name,
                'genre': book.genre.name,
                'get_absolute_url': book.get_absolute_url()
            })
        return result

    @staticmethod
    def get_by_id(id: int):
        return BookRepository.get_by_id(id)

    @staticmethod
    def create(title: str, price: float, amount: int, genre: int, author: int):
        return BookRepository.create(title, price, amount, genre, author)

    @staticmethod
    def update(id: int, title: str, price: float, amount: int, genre: int, author: int):
        return BookRepository.update(id, title, price, amount, genre, author)

    @staticmethod
    def delete(id: int):
        return BookRepository.delete(id)
