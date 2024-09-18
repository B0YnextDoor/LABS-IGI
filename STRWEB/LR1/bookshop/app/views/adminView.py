from django.shortcuts import redirect, render
from django.views import View
from app.core.validators import check_response
from app.services.emloyeeService import EmployeeService
from app.services.adminService import AdminService


class AdminView(View):
    template_name = 'admin.html'

    def get_admin(self, request):
        email = request.session.get('user')
        role = request.session.get('role')
        if check_response(email, request):
            return None, None
        user = EmployeeService.get_by_email(email)
        if check_response(user, request) or role != 'adm':
            return None, None
        return user, role

    def get(self, request):
        user, role = self.get_admin(request)
        if user is None:
            return redirect('main')
        books = AdminService.get_price_list()
        customers = AdminService.get_customers_list()
        most, least = AdminService.get_popular_goods()
        month_stats = AdminService.get_month_volume()
        income = AdminService.get_year_income()
        forecast = AdminService.get_forecast()
        return render(request, self.template_name, {'role': role, 'books': books, 'customers': customers,
                                                    'most': most, 'least': least, 'month_stats': month_stats,
                                                    'income': income, 'forecast': forecast, 'cart': request.session.get('cart')})
