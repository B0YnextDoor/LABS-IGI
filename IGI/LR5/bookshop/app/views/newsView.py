from django.http import Http404
from django import forms
from django.shortcuts import render, redirect
from django.views import View
from app.app_models.commonModels import News
from app.services.commonService import NewsService


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        exclude = ['id', 'created_at', 'updated_at']


class NewsView(View):
    template_name = 'news.html'

    def get(self, request):
        return render(request, self.template_name, {'role': request.session.get('role'),
                                                    'news': NewsService.get_all(), 'form': None})

    def post(self, request):
        if request.session.get('role') != 'adm':
            return redirect('news')
        if (request.POST.get('action') == 'add'):
            return render(request, self.template_name, {'role': request.session.get('role'), 'news': None,
                                                        'form': NewsForm()})
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                news = NewsService.create(form.cleaned_data['title'], form.cleaned_data['text'],
                                          form.cleaned_data['img'])
                if news is not None:
                    return redirect('news')
                form.add_error(None, 'Creating news error!')
            except:
                form.add_error(None, 'Creating news error!')
        return render(request, self.template_name, {'role': request.session.get('role'),
                                                    'news': NewsService.get_all(), 'form': form})


class NewsDetailView(View):
    template_name = 'news-detail.html'

    def get(self, request, id):
        news = NewsService.get_by_id(int(id))
        if news is None:
            return Http404('News not found')
        return render(request, self.template_name, {'role': request.session['role'], 'news': news, 'form': None})

    def post(self, request, id):
        if request.session.get('role') != 'adm':
            return redirect('news')
        news = NewsService.get_by_id(int(id))
        if (request.POST.get('action') == 'upd'):
            form = NewsForm(
                initial={'title': news.title, 'text': news.text, 'img': news.img})
            return render(request, self.template_name, {'role': request.session['role'], 'news': news, 'form': form})
        elif (request.POST.get('action') == 'del'):
            NewsService.delete(int(id))
            return redirect('news')
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                news = NewsService.update(int(id), form.cleaned_data['title'], form.cleaned_data['text'],
                                          form.cleaned_data['img'])
                if news is None:
                    form.add_error(None, 'Updating news error!')
                else:
                    form = None
            except:
                form.add_error(None, 'Updating news error!')
        return render(request, self.template_name, {'role': request.session.get('role'), 'news': news, 'form': form})
