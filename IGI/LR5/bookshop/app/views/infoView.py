from django.shortcuts import render, redirect
from django.views import View
from django import forms
from app.services.commonService import InfoService
from app.app_models.commonModels import AboutInfo


class InfoForm(forms.ModelForm):
    class Meta:
        model = AboutInfo
        fields = ['info']


class InfoView(View):
    template_name = 'about.html'

    def get(self, request):
        return render(request, self.template_name, {'role': request.session['role'], 'info': InfoService.get(),
                                                    'form': None})

    def post(self, request):
        if (request.session.get('role') != 'adm'):
            return redirect('about')
        if (request.POST.get('action') == 'upd'):
            return render(request, self.template_name, {'role': request.session['role'], 'info': None,
                                                        'form': InfoForm()})
        form = InfoForm(request.POST)
        info = InfoService.get()
        if form.is_valid():
            try:
                info = InfoService.update(form.cleaned_data['info'])
                if info is not None:
                    return redirect('about')
                form.add_error(None, 'Info update error')
            except:
                form.add_error(None, 'Info update error')
        return render(request, self.template_name, {'role': request.session['role'], 'info': info,
                                                    'form': form})
