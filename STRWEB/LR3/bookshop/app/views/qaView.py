from django import forms
from django.shortcuts import render, redirect
from django.views import View
from app.app_models.commonModels import QA
from app.services.commonService import QAService


class QAForm(forms.ModelForm):
    class Meta:
        model = QA
        exclude = ['id', 'created_at', 'updated_at']


class QAView(View):
    template_name = 'qa.html'

    def get(self, request):
        return render(request, self.template_name, {'role': request.session['role'], 'qas': QAService.get_all(), 'form': None, 'action': None, 'cart': request.session.get('cart')})

    def post(self, request):
        if request.session.get('role') != 'adm':
            return redirect('faq')
        if (request.POST.get('action') == 'add'):
            return render(request, self.template_name, {'role': request.session['role'], 'qas': None, 'form': QAForm(), 'action': 'add', 'cart': request.session.get('cart')})
        elif ('del' in request.POST.get('action')):
            QAService.delete(int(request.POST['action'].split('_')[1]))
            return redirect('faq')
        elif ('upd' in request.POST.get('action')):
            id = int(request.POST['action'].split('_')[1])
            qa = QAService.get_by_id(id)
            if qa is None:
                return redirect('faq')
            form = QAForm(
                initial={'question': qa.question, 'answer': qa.answer})
            return render(request, self.template_name, {'role': request.session['role'], 'qas': None, 'form': form, 'action': id, 'cart': request.session.get('cart')})
        form = QAForm(request.POST)
        action = request.POST['action'].split('_')[1]
        if form.is_valid():
            try:
                if (action == 'add'):
                    qa = QAService.create(
                        form.cleaned_data['question'], form.cleaned_data['answer'])
                else:
                    qa = QAService.update(int(action),
                                          form.cleaned_data['question'], form.cleaned_data['answer'])
                if qa is not None:
                    return redirect('faq')
                form.add_error(None, f'DB error')
            except:
                form.add_error(None, f'DB error')
        return render(request, self.template_name, {'role': request.session['role'], 'qas': None, 'form': form, 'action': action, 'cart': request.session.get('cart')})
