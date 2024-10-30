from django.shortcuts import render, redirect
from django.views import View
from django import forms
from app.services.commonService import InfoService
from app.app_models.commonModels import AboutInfo


class InfoForm(forms.ModelForm):
    class Meta:
        model = AboutInfo
        fields = ['info', 'logo', 'video',
                  'history', 'requisites', 'certificate']


class InfoView(View):
    template_name = 'about.html'

    def get(self, request):
        info = InfoService.get()
        info['certificate'] = info['certificate'].split('\n')
        return render(request, self.template_name, {'role': request.session['role'],
                                                    'info': info,
                                                    'form': None, 'cart': request.session.get('cart')})

    def post(self, request):
        info = InfoService.get()
        if (request.session.get('role') != 'adm'):
            return redirect('about')
        if (request.POST.get('action') == 'upd'):
            form = InfoForm(initial={'info': info['info'], 'logo': info['logo'], 'video': info['video'],
                                     'history': info['history'], 'requisites': info['requisites'],
                                     'certificate': info['certificate']})
            return render(request, self.template_name, {'role': request.session['role'], 'info': info,
                                                        'form': form,
                                                        'cart': request.session.get('cart')})
        form = InfoForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                info = InfoService.update(info=form.cleaned_data['info'], logo=form.cleaned_data['logo'],
                                          video=form.cleaned_data['video'], history=form.cleaned_data['history'],
                                          requisites=form.cleaned_data['requisites'],
                                          certificate=form.cleaned_data['certificate'])
                if info is not None:
                    return redirect('about')
                form.add_error(None, 'Info update error')
            except:
                form.add_error(None, 'Info update error')
        return render(request, self.template_name, {'role': request.session['role'], 'info': info,
                                                    'form': form, 'cart': request.session.get('cart')})
