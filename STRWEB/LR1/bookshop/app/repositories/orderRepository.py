from datetime import datetime
from app.app_models.customerModel import Customer
from app.app_models.orderModels import Order, OrderInfo
from app.app_models.bookModels import Book
from collections import Counter


class OrderRepository:
    @staticmethod
    def check_orders_status(user=None):
        orders = Order.objects.all() if user is None else Order.objects.filter(customer_id=user)
        for order in orders:
            if order.orderinfo.status == '0' and order.orderinfo.delivery_date.date() <= datetime.today().date():
                db_info = OrderInfo.objects.get(order_id=order)
                db_info.status = '1'
                db_info.save()

    @staticmethod
    def get_books_quantity(db_order, order_books: list):
        books = []
        for book in order_books:
            book_ammount = db_order.goods.through.objects.get(
                order=db_order, book=book)
            book.quantity = book_ammount.quantity
            books.append(book)
        return books

    @staticmethod
    def get_all():
        try:
            OrderRepository.check_orders_status()
            db_orders = Order.objects.all()
            orders = list()
            for ord in db_orders:
                books = OrderRepository.get_books_quantity(
                    ord, ord.goods.all())
                orders.append({'id': ord.id, 'books': books, 'status': ord.orderinfo.status,
                               'date': ord.orderinfo.delivery_date.date(), 'address': ord.orderinfo.delivery_address, 'price': round(ord.orderinfo.order_price, 2),
                               'created_at': ord.created_at.date(), 'sale': ord.orderinfo.sale,
                               'customer': {'name': ord.customer_id.name, 'phone': ord.customer_id.phone,
                                            'email': ord.customer_id.email}})
            return orders
        except:
            return None

    @staticmethod
    def get_user_orders(user):
        try:
            OrderRepository.check_orders_status(user)
            db_orders = user.order_set.all()
            orders = list()
            for id, ord in enumerate(db_orders):
                books = OrderRepository.get_books_quantity(
                    ord, ord.goods.all())
                orders.append({'id': ord.id, 'cl_id': id + 1, 'books': books, 'status': ord.orderinfo.status,
                               'date': ord.orderinfo.delivery_date.date(), 'address': ord.orderinfo.delivery_address,
                               'method': ord.get_absolute_url})
            return orders
        except Exception as e:
            print(e)
            return None

    @staticmethod
    def get_by_id(id: int):
        try:
            order = Order.objects.filter(id=id).first()
            if order is None:
                return None
            books = OrderRepository.get_books_quantity(
                order, order.goods.all())
            return {'id': order.id, 'books': books, 'status': order.orderinfo.status,
                    'date': order.orderinfo.delivery_date.date(), 'price': round(order.orderinfo.order_price, 2),
                    'address': order.orderinfo.delivery_address, 'sale': order.orderinfo.sale,
                    'created_at': order.created_at.date()}
        except Exception as e:
            print(e)
            return None

    @staticmethod
    def create_order(email: str, book_ids: list[str], date: datetime, adress: str, sale: float):
        try:
            db_user = Customer.objects.filter(email=email).first()
            if db_user is None:
                return None
            new_order = Order.objects.create(
                customer_id=db_user)
            order_price = 0
            count = Counter(book_ids)
            for id, q in count.items():
                book = Book.objects.filter(id=int(id)).first()
                if book is not None and book.amount > 0:
                    order_price += book.price * q
                    new_order.goods.add(book, through_defaults={'quantity': q})
                    book.amount -= q
                    book.save()
            new_order.save()
            OrderInfo.objects.create(
                order_id=new_order, delivery_date=date, delivery_address=adress, order_price=order_price*(1-sale), sale=sale*100).save()
            return new_order
        except Exception as e:
            print(e)
            return None

    @staticmethod
    def update_books(db_order):
        for book in db_order.goods.all():
            db_book = Book.objects.get(id=book.id)
            book_ammount = db_order.goods.through.objects.get(
                order=db_order, book=db_book)
            db_book.amount += book_ammount.quantity
            db_book.save()
        db_order.goods.clear()

    @staticmethod
    def update_order(id: int, book_ids: list[str], date: datetime, address: str, sale: float):
        try:
            db_order = Order.objects.filter(id=id).first()
            if db_order is None:
                return None
            OrderRepository.update_books(db_order)
            db_order_info = OrderInfo.objects.get(order_id=db_order)
            order_price = 0
            count = Counter(book_ids)
            for book_id, q in count.items():
                book = Book.objects.filter(id=int(book_id)).first()
                if book is not None and book.amount > 0:
                    order_price += book.price * q
                    db_order.goods.add(book, through_defaults={'quantity': q})
                    book.amount -= q
                    book.save()
            db_order.save()
            db_order_info.order_id = db_order
            db_order_info.delivery_date = date
            db_order_info.delivery_address = address
            db_order_info.order_price = order_price*(1-sale)
            db_order_info.sale = sale*100
            db_order_info.save()
            return db_order
        except Exception as e:
            print(e)
            return None

    @staticmethod
    def cancel_order(id: int):
        try:
            db_order = Order.objects.filter(id=id).first()
            if db_order is None:
                return None
            OrderRepository.update_books(db_order)
            db_order_info = OrderInfo.objects.get(order_id=db_order)
            db_order_info.status = '2'
            db_order_info.save()
            db_order.save()
            return 'ok'
        except:
            return None
