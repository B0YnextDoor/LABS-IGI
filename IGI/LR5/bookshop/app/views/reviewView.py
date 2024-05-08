from django import forms
from django.shortcuts import render, redirect
from django.views import View
from app.services.userService import UserService
from app.app_models.customerModel import CustomerReview


class ReviewForm(forms.ModelForm):
    def clean_rate(self):
        try:
            data = int(self.cleaned_data.get('rate'))
            if data is None or data < 0 or data > 5:
                self.add_error(
                    None, 'Rate must be an integer number in range 0-5')
                return 0
        except:
            self.add_error(None, 'Rate must be an integer number in range 0-5')
            return 0
        return data

    class Meta:
        model = CustomerReview
        fields = ['rate', 'text']


class ReviewView(View):
    template_name = 'review.html'

    def get_user(self, request):
        return request.session.get('user'), request.session.get('role')

    def get(self, request):
        email, role = self.get_user(request)
        return render(request, self.template_name, {'role': role, 'email': email,
                                                    'reviews': UserService.get_reviews(), 'form': None, 'action': None})

    def post(self, request):
        if (request.session.get('role') == '' or request.POST.get('action') == 'redir'):
            return redirect('signin')
        email, role = self.get_user(request)
        if role != 'usr':
            return redirect('reviews')
        if (request.POST.get('action') == 'add'):
            return render(request, self.template_name, {'role': request.session['role'], 'reviews': None,
                                                        'form': ReviewForm(), 'action': 'add', 'email': email})
        if ('del' in request.POST.get('action')):
            id = int(request.POST['action'].split('_')[1])
            rev = UserService.get_review_by_id(id)
            if rev is not None and rev.user.email == email:
                UserService.delete_review(id)
            return redirect('reviews')
        elif ('upd' in request.POST.get('action')):
            id = int(request.POST['action'].split('_')[1])
            rev = UserService.get_review_by_id(id)
            if rev is None or rev.user.email != email:
                return redirect('reviews')
            form = ReviewForm(
                initial={'rate': rev.rate, 'text': rev.text})
            return render(request, self.template_name, {'role': request.session['role'], 'reviews': None,
                                                        'form': form, 'action': id, 'email': email})
        form = ReviewForm(request.POST)
        action = request.POST['action'].split('_')[1]
        if form.is_valid():
            try:
                if (action == 'add'):
                    rev = UserService.create_review(
                        email, form.cleaned_data['rate'], form.cleaned_data['text'])
                else:
                    rev = UserService.update_review(
                        int(action), form.cleaned_data['rate'], form.cleaned_data['text'])
                if rev is None:
                    form.add_error(None, f'DB error')
                else:
                    form = None
                    return redirect('reviews')
            except:
                form.add_error(None, f'DB error')
        return render(request, self.template_name, {'role': role, 'email': email,
                                                    'reviews': None, 'form': form, 'action': action})
