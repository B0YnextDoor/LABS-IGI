from django.shortcuts import redirect, render
from django import forms
from django.views import View
from datetime import datetime, timezone
from calendar import month
from app.core.validators import check_response, phone_validator, password_validator
from app.services.userService import UserService
from app.services.orderService import OrderService
from app.services.emloyeeService import EmployeeService
from app.app_models.customerModel import Customer


class UserForm(forms.ModelForm):
    def clean(self):
        phone_validator(self.cleaned_data['phone'], self)
        password_validator(self.cleaned_data['password'], self)
        return self.cleaned_data

    class Meta:
        model = Customer
        exclude = ['id', 'created_at', 'updated_at']
        widgets = {
            'password': forms.PasswordInput()
        }


class AccountView(View):
    template_name = 'account.html'

    def get_user(self, request):
        email = request.session.get('user')
        role = request.session.get('role')
        if check_response(email, request):
            return None, None, None
        user = UserService.get_by_email(
            email) if role == 'usr' else EmployeeService.get_by_email(email)
        if check_response(user, request):
            return None, None, None
        date_utc = datetime.now(timezone.utc)
        date_local = date_utc.astimezone()
        user_info = {'name': user.name,
                     'email': user.email, 'phone': user.phone,
                     'tz': f'{str(date_local.tzinfo).split(" ")[0]} / {str(date_local.utcoffset())[:-3]}',
                     'date_utc': date_utc.strftime('%d/%m/%Y %H:%M'),
                     'date_local': date_local.strftime('%d/%m/%Y %H:%M'),
                     'calendar': month(date_local.year, date_local.month)}
        if role == 'usr':
            acc_info = OrderService.get_user_orders(user)
            if check_response(acc_info, request):
                return None, None, None
            user_info.update({'orders': acc_info})
        return user, role, user_info

    def get(self, request):
        user, role, user_info = self.get_user(request)
        if user is None:
            return redirect('main')
        return render(request, self.template_name, {'role': role, 'user': user_info, 'form': None})

    def post(self, request):
        user, role, user_info = self.get_user(request)
        if user is None:
            return redirect('main')
        if (request.POST.get('action') == 'editMe'):
            form = UserForm(
                initial={'name': user.name, 'phone': user.phone, 'email': user.email})
            return render(request, self.template_name, {'role': role, 'user': user_info, 'form': form})
        form = UserForm(request.POST)
        if form.is_valid():
            try:
                if role == 'usr':
                    upd_user = UserService.update(user.email, form.data['name'], form.data['phone'],
                                                  form.data['email'], form.data['password'])
                else:
                    upd_user = EmployeeService.update(user.email, form.data['name'], form.data['phone'],
                                                      form.data['email'], form.data['password'])
                if upd_user is None:
                    form.add_error(None, 'Edit error!')
                elif type(upd_user) == str:
                    form.add_error(None, upd_user)
                else:
                    request.session['user'] = upd_user.email
                    request.session.save()
                    return redirect('account')
            except:
                form.add_error(None, 'Edit error!')
        return render(request, self.template_name, {'role': role, 'user': user_info, 'form': form})
