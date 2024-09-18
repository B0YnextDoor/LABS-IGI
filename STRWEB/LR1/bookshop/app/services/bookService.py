from app.repositories.bookRepository import BookRepository


class BookService:
    @staticmethod
    def get_all(param: str):
        return BookRepository.get_all(param)

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
