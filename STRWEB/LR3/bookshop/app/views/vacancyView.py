from django import forms
from django.shortcuts import render, redirect
from django.views import View
from app.services.commonService import VacancyService
from app.app_models.commonModels import Vacancy


class VacancyForm(forms.ModelForm):
    class Meta:
        model = Vacancy
        fields = ['name', 'description']


class VacancyView(View):
    template_name = 'vacancy.html'

    def get(self, request):
        return render(request, self.template_name, {'role': request.session.get('role'), 'action': None,
                                                    'vacancies': VacancyService.get_all(), 'form': None,
                                                    'cart': request.session.get('cart')})

    def post(self, request):
        if request.session.get('role') != 'adm':
            return redirect('vacancies')
        if (request.POST.get('action') == 'add'):
            form = VacancyForm(
                initial={'description': 'Requirements:\nSalary:'})
            return render(request, self.template_name, {'role': request.session.get('role'), 'vacancies': None,
                                                        'form': form, 'action': 'add', 'cart': request.session.get('cart')})
        elif ('del' in request.POST.get('action')):
            VacancyService.delete(int(request.POST['action'].split('_')[1]))
            return redirect('vacancies')
        elif ('upd' in request.POST.get('action')):
            id = int(request.POST['action'].split('_')[1])
            vac = VacancyService.get_by_id(id)
            if vac is None:
                return redirect('vacancies')
            form = VacancyForm(
                initial={'name': vac.name, 'description': vac.description})
            return render(request, self.template_name, {'role': request.session['role'], 'vacancies': None,
                                                        'form': form, 'action': id, 'cart': request.session.get('cart')})
        form = VacancyForm(request.POST)
        action = request.POST['action'].split('_')[1]
        if form.is_valid():
            try:
                if (action == 'add'):
                    vac = VacancyService.create(
                        form.cleaned_data['name'], form.cleaned_data['description'])
                else:
                    vac = VacancyService.update(int(action),
                                                form.cleaned_data['name'], form.cleaned_data['description'])
                if vac is None:
                    form.add_error(None, f'DB error')
                else:
                    form = None
                    return redirect('vacancies')
            except:
                form.add_error(None, f'DB error')
        return render(request, self.template_name, {'role': request.session['role'], 'vacancies': None,
                                                    'form': form, 'action': action, 'cart': request.session.get('cart')})
