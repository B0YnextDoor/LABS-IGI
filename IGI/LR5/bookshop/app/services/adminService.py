from app.services import bookService, orderService
from datetime import datetime
from collections import Counter
from matplotlib import pyplot as plt
from numpy import polyfit, array


class AdminService:
    orders = None
    books = None
    sales = list()

    @staticmethod
    def get_price_list():
        AdminService.books = bookService.BookService.get_all('amount')
        return AdminService.books

    @staticmethod
    def draw_customers_stat(customers):
        plt.bar(customers.keys(), [
                len(value) for value in customers.values()], width=0.5, color='blue')
        plt.xlabel('Cities')
        plt.ylabel('Amount of clients')
        plt.title('Customers statistics')
        plt.savefig('./app/static/images/customers_stat.jpg')
        plt.clf()

    @staticmethod
    def get_customers_list():
        AdminService.orders = [
            order for order in orderService.OrderService.get_all() if order['status'] != '2']
        customers = dict()
        for order in AdminService.orders:
            city = order['address'].split(',')[0]
            customer = order['customer']
            if city not in customers.keys():
                customers[city] = [customer]
            elif customer not in customers[city]:
                customers[city].append(customer)
        AdminService.draw_customers_stat(customers)
        return customers

    @staticmethod
    def get_orders_counter(condion=None):
        orders = AdminService.orders if condion is None else \
            [order for order in AdminService.orders if condion(order)]
        if condion is not None and len(orders) == 0:
            return orders
        books = list()
        for order in orders:
            books.extend(order['books'])
        counter = Counter(books)
        for book in AdminService.books:
            if book not in counter.keys() and book.amount > 0:
                counter[book] = 0
        return counter.most_common()

    @staticmethod
    def get_all_popular(common, counter, k, func=lambda x: x + 1):
        while abs(k) < len(counter) and common[-1][1] == counter[k][1]:
            common.append(counter[k])
            k = func(k)
        return common

    @staticmethod
    def get_popular_goods():
        counter = AdminService.get_orders_counter()
        most_common = AdminService.get_all_popular([counter[0]], counter, 1)
        least_common = list()
        if most_common[0][1] != counter[-1][1]:
            least_common = AdminService.get_all_popular(
                [counter[-1]], counter, -2, lambda x: x - 1)
        return most_common, least_common

    @staticmethod
    def draw_month_stats(months, sales, incomes):
        plt.bar(months, sales)
        plt.xlabel('Months')
        plt.ylabel('Sales amount')
        plt.title('Amount of sales per month')
        plt.savefig('./app/static/images/month_volumes_stat.jpg')
        plt.clf()
        plt.bar(months, incomes)
        plt.xlabel('Months')
        plt.ylabel('Incomes amount')
        plt.title('Incomes per month')
        plt.savefig('./app/static/images/month_incomes_stat.jpg')
        plt.clf()

    @staticmethod
    def get_month_volume():
        counters = dict()
        months = list()
        sales = list()
        incomes = list()
        for i in range(1, datetime.now().month + 1):
            month_name = datetime(1, i, 1).strftime('%B')
            counters[month_name] = AdminService.get_orders_counter(
                lambda o: o['created_at'].month == i)
            months.append(month_name[:3] if len(
                month_name) > 4 else month_name)
            month_sale = 0
            month_incomes = 0
            for book, sale in counters[month_name]:
                month_sale += sale
                month_incomes += float(sale * book.price)
            sales.append(month_sale)
            incomes.append(month_incomes)
        AdminService.draw_month_stats(months, sales, incomes)
        AdminService.sales = sales
        return counters

    @staticmethod
    def get_year_income():
        return round(float(sum([order['price'] for order in AdminService.orders if order['created_at'].year == datetime.now().year])), 2)

    @staticmethod
    def get_forecast():
        if len(AdminService.sales) == 0:
            return 0
        months = array(range(1, datetime.now().month + 1))
        a, b = polyfit(months, AdminService.sales, 1)
        plt.plot(months, a*months + b, marker='o', markersize=5,
                 linestyle='-', label=f'Linear trend: y = {round(a,2)}x + {round(b,2)}')
        plt.xlabel('Months')
        plt.ylabel('Sales amount')
        plt.title('Linear sales trend')
        plt.legend()
        plt.savefig('./app/static/images/sales_trend.jpg')
        plt.clf()
        return sum(AdminService.sales) / len(AdminService.sales)
