from django.http import Http404
from django.shortcuts import redirect, render
from django import forms
from django.views import View
from datetime import datetime, timedelta
from app.core.validators import check_response
from app.services.bookService import BookService
from app.services.orderService import OrderService
from app.services.saleService import SaleService


class CustomCheckbox(forms.CheckboxSelectMultiple):
    def create_option(self, name, value, label, selected, index, subindex=None, attrs=None):
        option_dict = super().create_option(name, value, label, selected,
                                            index, subindex=subindex, attrs=attrs)
        option_dict['attrs']['data-price'] = label.split(' ')[-2]
        return option_dict


class OrderForm(forms.Form):
    books = forms.MultipleChoiceField(choices=list(map(
        lambda b: (
            b.id, f'{b.title}, {b.author.surname} {b.author.name}, {b.price} BYN'),
        filter(lambda b: b.amount > 0, BookService.get_all('amount')))),
        required=True, error_messages={'required': 'Choose at least 1 book'},
        widget=CustomCheckbox)
    date = forms.DateField(
        required=True, error_messages={'required': 'Enter a date'},
        widget=forms.SelectDateWidget,
        initial=datetime.today().date() + timedelta(days=1))
    address = forms.CharField(required=True, initial='Minsk, M. Bogdanovich 29',
                              error_messages={
                                  'required': 'Enter a delivery address'},
                              help_text='Enter a delivery address(pickup address as default)')
    sale_code = forms.CharField(max_length=10, required=False)

    def clean_books(self):
        data = self.cleaned_data['books']
        if len(data) == 0:
            self.add_error(None, 'Choose at least 1 book')
            return 'err'
        return data

    def clean_date(self):
        data = self.cleaned_data['date']
        if data <= datetime.today().date():
            self.add_error(None, 'The date cannot be in the past!')
            return 'err'
        return data

    def clean_address(self):
        data = self.cleaned_data['address']
        address = data.split(',')
        if len(address) == 1 or address[0].strip().isdigit() or len(address[0].strip()) == 0 or \
                address[1].strip().isdigit() or len(address[1]) == 0:
            self.add_error(None, 'Address must match: `city`,`street`')
            return 'err'
        return data

    def clean_sale_code(self):
        data = self.cleaned_data['sale_code']
        if len(data) and not SaleService.check_code(data):
            self.add_error(None, 'Sale code doesn\'t exist')
            return 'err'
        return data


class OrderView(View):
    template_name = 'order.html'

    def get(self, request):
        role = request.session.get('role')
        if role != 'adm' and role != 'emp':
            return redirect('main')
        return render(request, self.template_name, {'role': role, 'form': None, 'orders': OrderService.get_all()})

    def post(self, request):
        email = request.session.get('user')
        role = request.session.get('role')
        if check_response(email, request) or role != 'usr':
            return redirect('main')
        if ('buy' in request.POST.get('action')):
            id = request.POST['action'].split('_')[1]
            if id not in request.session['cart']:
                request.session['cart'].append(id)
                request.session.save()
            return redirect('catalog')
        elif (request.POST.get('action') == 'cart'):
            books = request.session['cart']
            print(books)
            form = OrderForm(initial={'books': books})
            return render(request, self.template_name, {'role': role, 'form': form, 'orders': None})
        form = OrderForm(request.POST)
        if form.is_valid():
            try:
                sale = 0
                if form.cleaned_data['sale_code']:
                    sale = float(
                        form.cleaned_data['sale_code'].split('_')[1])/100
                order = OrderService.create_order(
                    email, form.cleaned_data['books'], form.cleaned_data['date'], form.cleaned_data['address'], sale
                )
                if order is not None:
                    request.session['cart'] = []
                    return redirect('account')
                form.add_error(None, "Order creation error!")
            except:
                form.add_error(None, "Order creation error!")
        return render(request, self.template_name, {'role': role, 'form': form, 'orders': None})


class OrderDetailView(View):
    context_object_name = 'order'
    template_name = 'order-detail.html'

    def get_order(self, id: int):
        return OrderService.get_by_id(id)

    def get(self, request, id):
        if request.session.get('role') != 'usr':
            return redirect('main')
        order = self.get_order(id)
        if order is None:
            raise Http404("Order does not exist")
        return render(request, self.template_name, {'role': request.session['role'], 'order': order, 'form': None})

    def post(self, request, id):
        if request.session.get('role') != 'usr':
            return self.get(request, id)
        order = self.get_order(id)
        if request.POST.get('action') == 'edit':
            form = OrderForm(initial={'books': list(map(lambda b: str(b.id), order['books'])),
                                      'date': order['date'], 'address': order['address']})
            return render(request, self.template_name, {'role': request.session['role'], 'order': order, 'form': form})
        elif request.POST.get('action') == 'del':
            OrderService.cancel_order(int(id))
            return redirect('account')
        form = OrderForm(request.POST)
        if form.is_valid():
            try:
                sale = 0
                if form.cleaned_data['sale_code']:
                    sale = float(
                        form.cleaned_data['sale_code'].split('_')[1])/100
                order = OrderService.update_order(int(id), form.cleaned_data['books'],
                                                  form.cleaned_data['date'], form.cleaned_data['address'], sale)
                if order is None:
                    form.add_error(None, 'Order update error!')
                else:
                    form = None
                    return redirect('account')
            except:
                form.add_error(None, 'Order update error!')
        return render(request, self.template_name, {'role': request.session['role'], 'order': order, 'form': form})
