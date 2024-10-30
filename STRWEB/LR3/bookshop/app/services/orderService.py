from app.repositories.orderRepository import OrderRepository, datetime


class OrderService:
    @staticmethod
    def get_all():
        return OrderRepository.get_all()

    @staticmethod
    def get_user_orders(user):
        return OrderRepository.get_user_orders(user)

    @staticmethod
    def get_by_id(id: int):
        return OrderRepository.get_by_id(id)

    @staticmethod
    def create_order(email: str, book_ids: list[str], date: datetime.date, address: str, sale: float):
        return OrderRepository.create_order(email, book_ids, date, address, sale)

    @staticmethod
    def update_order(id: int, book_ids: list[str], date: datetime.date, address: str, sale: float):
        return OrderRepository.update_order(id, book_ids, date, address, sale)

    @staticmethod
    def cancel_order(id: int):
        return OrderRepository.cancel_order(id)
