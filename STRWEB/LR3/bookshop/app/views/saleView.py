from django.shortcuts import redirect, render
from django import forms
from django.views import View
from app.app_models.commonModels import SaleCode
from app.services.saleService import SaleService


class SaleCodeForm(forms.ModelForm):
    def clean_code(self):
        data = self.cleaned_data['code']
        sale = data.split('_')
        if len(sale) == 1:
            self.add_error(
                None, 'Sale code must match `code-part`_`sale-part`')
            return 'err'
        if len(sale[1]) > 2:
            self.add_error(None, 'Sale must be less 100')
            return 'err'
        return data

    class Meta:
        model = SaleCode
        exclude = ['id', 'created_at', 'updated_at']


class SaleCodeView(View):
    template_name = 'salecodes.html'

    def get(self, request):
        role = request.session.get('role')
        if role is None:
            return redirect('main')
        if role == 'adm':
            codes = SaleService.get_all()
        else:
            codes = SaleService.get_active()
        return render(request, self.template_name, {'role': role, 'codes': codes, 'form': None,
                                                    'cart': request.session.get('cart')})

    def post(self, request):
        role = request.session.get('role')
        if role != 'adm':
            return redirect('sale')
        if request.POST.get('action') == 'add':
            form = SaleCodeForm()
            return render(request, self.template_name, {'role': role, 'codes': None, 'form': form,
                                                        'cart': request.session.get('cart')})
        elif 'upd' in request.POST.get('action'):
            SaleService.update(int(request.POST['action'].split('_')[1]))
            return redirect('sale')
        elif 'del' in request.POST.get('action'):
            SaleService.delete(int(request.POST['action'].split('_')[1]))
            return redirect('sale')
        else:
            form = SaleCodeForm(request.POST)
            if form.is_valid():
                try:
                    code = SaleService.create(
                        form.cleaned_data['code'], form.cleaned_data['is_active'])
                    if code is not None:
                        return redirect('sale')
                    form.add_error(None, 'Creation error')
                except:
                    form.add_error(None, 'Creation error')
            return render(request, self.template_name, {'role': role, 'codes': SaleService.get_all(), 'form': form, 'cart': request.session.get('cart')})
