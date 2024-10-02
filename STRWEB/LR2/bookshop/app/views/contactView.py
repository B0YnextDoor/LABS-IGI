from django import forms
from django.shortcuts import render, redirect
from django.views import View
from app.services.emloyeeService import EmployeeService


class InfoCreateForm(forms.Form):
    employee = forms.ChoiceField(required=True,
                                 choices=list(map(lambda e: (
                                     e.id, f'{e.name}, {e.phone}, {e.email}'),
                                     EmployeeService.get_info()[1])))
    image = forms.ImageField(required=True, help_text='Employees photo')
    description = forms.CharField(
        required=True, help_text='Work description', widget=forms.Textarea,
        error_messages={'required': 'Description is required!'})


class InfoUpdateForm(forms.Form):
    image = forms.ImageField(required=True, help_text='Employees photo')
    description = forms.CharField(
        required=True, help_text='Work description', widget=forms.Textarea,
        error_messages={'required': 'Description is required!'})


class EmployeeInfoView(View):
    template_name = 'contacts.html'

    def get(self, request):
        has_info, no_info = EmployeeService.get_info()
        return render(request, self.template_name, {'role': request.session['role'], 'form': None,
                                                    'employees': has_info, 'action': None, 'no_info': no_info,
                                                    'cart': request.session.get('cart')})

    def post(self, request):
        role = request.session.get('role')
        if role != 'adm':
            return redirect('contacts')
        if (request.POST.get('action') == 'add'):
            return render(request, self.template_name, {'role': request.session['role'], 'form': InfoCreateForm(),
                                                        'employees': None, 'action': 'add', 'cart': request.session.get('cart'), 'form_type': '-add'})
        elif ('upd' in request.POST.get('action')):
            id = request.POST['action'].split('_')[1]
            empl = EmployeeService.get_by_id(int(id))
            if empl is None:
                return redirect('contacts')
            form = InfoUpdateForm(initial={'image': empl.employeeinfo.img,
                                           'description': empl.employeeinfo.description})
            return render(request, self.template_name, {'role': request.session['role'], 'form': form,
                                                        'employees': None, 'action': empl.id, 'cart': request.session.get('cart'), 'form_type': ''})
        action = request.POST.get('action').split('_')[1]
        if action == 'add':
            form = InfoCreateForm(request.POST, request.FILES)
        else:
            form = InfoUpdateForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                if action == 'add':
                    info = EmployeeService.add_info(int(form.cleaned_data['employee']), form.cleaned_data['image'],
                                                    form.cleaned_data['description'])
                else:
                    info = EmployeeService.update_info(int(action), form.cleaned_data['image'],
                                                       form.cleaned_data['description'])
                if info is not None:
                    return redirect('contacts')
                form.add_error(None, 'DB error')
            except:
                form.add_error(None, 'DB error')
        return render(request, self.template_name, {'role': request.session['role'], 'form': form,
                                                    'employees': None, 'action': action,
                                                    'cart': request.session.get('cart')})
