from django import forms
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views import View
from app.services.emloyeeService import EmployeeService


class InfoUpdateForm(forms.Form):
    image = forms.ImageField(help_text='Employees photo')
    description = forms.CharField(
        required=True, help_text='Work description', widget=forms.Textarea,
        error_messages={'required': 'Description is required!'})

    def clean_image(self):
        return self.cleaned_data.get('image')

    def clean(self):
        data = self.cleaned_data.get('description')
        if data is None or len(data) == 0:
            self.add_error(None, 'Description is required!')
            return "err"
        return self.cleaned_data


class EmployeeInfoView(View):
    template_name = 'contacts.html'

    def get_queryset(self, role: str, page: int, sort_by: str | None, filter: str | None):
        result = EmployeeService.get_info(page, sort_by, filter)
        result['role'] = role
        return result

    def get(self, request):
        ids = request.GET.get("ids")
        if (ids is not None):
            return JsonResponse(EmployeeService.get_by_ids(str(ids).split(',')))
        page = request.GET.get("page")
        sort_by = request.GET.get("sort")
        filter = request.GET.get("filter")
        if (page is not None or sort_by is not None or filter is not None):
            return JsonResponse(self.get_queryset(request.session['role'], int(page), sort_by, filter))
        return render(request, self.template_name, {'role': request.session['role'], 'form': None,
                                                    'cart': request.session.get('cart')})

    def post(self, request):
        role = request.session.get('role')
        if role != 'adm':
            return redirect('contacts')
        action = request.POST.get('action')
        print(request.POST)
        print(request.FILES)
        if action is None:
            new_emp = EmployeeService.create(request.POST.get(
                "name"), request.POST.get('phone'), request.POST.get('email'))
            if new_emp is None:
                return JsonResponse({"error": 'Creating employee error'})
            info = EmployeeService.add_info(
                new_emp.id, request.FILES['image'], request.POST['description'])
            if info is None:
                return JsonResponse({"error": 'Creating employee error'})
            return JsonResponse(self.get_queryset(request.session['role'], 0, None, None))
        if ('upd' in action):
            id = request.POST['action'].split('_')[1]
            empl = EmployeeService.get_by_id(int(id))
            if empl is None:
                return redirect('contacts')
            form = InfoUpdateForm(initial={'image': empl.employeeinfo.img,
                                           'description': empl.employeeinfo.description})
            return render(request, self.template_name, {'role': request.session['role'], 'form': form,
                                                        'action': empl.id, 'cart': request.session.get('cart')})
        else:
            action = action.split('_')[1]
            form = InfoUpdateForm(initial={'image': request.FILES.get(
                'image'), 'description': request.POST.get('description')})
            try:
                info = EmployeeService.update_info(int(action), request.FILES.get(
                    'image'), request.POST.get('description'))
                if info is not None:
                    return redirect('contacts')
                form.add_error(None, 'Update info error')
            except:
                form.add_error(None, 'Update info error')
            return render(request, self.template_name, {'role': request.session['role'], 'form': form,
                                                        'action': action,
                                                        'cart': request.session.get('cart')})
