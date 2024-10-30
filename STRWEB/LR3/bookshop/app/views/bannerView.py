from django.shortcuts import render
from django.http import JsonResponse
from django import forms
from django.views import View
from app.app_models.commonModels import BannerSettings
from app.services.commonService import BannerService
from django.views.decorators.clickjacking import xframe_options_exempt


class SettingsForm(forms.ModelForm):
    def clean_delay(self):
        delay = self.cleaned_data.get('delay')
        if delay is None:
            self.add_error(None, 'Dealy is required!')
            return "err"
        if delay < 0:
            self.add_error(None, 'Delay must be positive number!')
            return "err1"
        elif delay > 60:
            self.add_error(None, "Delay max value is 60 seconds!")
            return "err2"
        return delay

    class Meta:
        model = BannerSettings
        exclude = ['id', 'created_at', 'updated_at']


class BannerView(View):
    template_name = 'banner.html'

    @xframe_options_exempt
    def get(self, request):
        if (request.GET.get('settings') is not None):
            return JsonResponse(BannerService.get())
        return render(request, self.template_name, {'cart': request.session.get('cart'),
                                                    'role': request.session.get('role'), 'form': None})

    def post(self, request):
        if (request.POST.get('action') == 'update'):
            settings = BannerService.get()
            form = SettingsForm(initial=settings)
            return render(request, self.template_name, {'cart': request.session.get('cart'),
                                                        'role': request.session.get('role'), 'form': form})
        form = SettingsForm(request.POST)
        if form.is_valid():
            try:
                settings = BannerService.update(form.cleaned_data.get('loop'), form.cleaned_data.get('navs'),
                                                form.cleaned_data.get(
                                                    'pags'), form.cleaned_data.get('auto'),
                                                form.cleaned_data.get('stopMouseHover'), form.cleaned_data.get('delay'))
                if settings is not None:
                    form = SettingsForm(initial=settings)
                else:
                    form.add_error(None, "Banner settings update error!")
            except:
                form.add_error(None, "Banner settings update error!")
        return render(request, self.template_name, {'cart': request.session.get('cart'),
                                                    'role': request.session.get('role'), 'form': form})
