from django.shortcuts import redirect, render
from django import forms
from django.views import View
from app.app_models.customerModel import Customer
from app.core.validators import phone_validator, password_validator, check_session
from app.services.authService import AuthService


class SignUpForm(forms.ModelForm):
    confirmation = forms.BooleanField(
        help_text='I confirm that I am over 18 years old.', required=True)

    def clean(self):
        phone_validator(self.cleaned_data['phone'], self)
        password_validator(self.cleaned_data['password'], self)
        return self.cleaned_data

    class Meta:
        model = Customer
        exclude = ['id', 'created_at', 'updated_at']
        widgets = {
            'password': forms.PasswordInput()
        }


class SignInForm(forms.ModelForm):
    def clean(self):
        return self.cleaned_data

    class Meta:
        model = Customer
        fields = ['email', 'password']
        widgets = {
            'password': forms.PasswordInput()
        }


class SignUpView(View):
    def get(self, request):
        check_session(request.session)
        form = SignUpForm(initial={'phone': '+37529'})
        return render(request, 'auth.html', {'form': form, 'type': 'Up', 'role': request.session['role']})

    def post(self, request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            try:
                user = AuthService.sign_up(form.data['name'], form.data['phone'],
                                           form.data['email'], form.data['password'])
                if type(user) == str:
                    form.add_error(None, user)
                elif user is not None:
                    request.session['role'] = 'usr'
                    request.session['user'] = user.email
                    request.session.modified = True
                    return redirect('main')
                else:
                    form.add_error(None, 'Sign Up error!')
            except:
                form.add_error(None, 'Sign Up error!')
        return render(request, 'auth.html', {'form': form, 'type': 'Up', 'role': request.session['role']})


class SignInView(View):
    def get(self, request):
        form = SignInForm()
        return render(request, 'auth.html', {'form': form, 'type': 'In', 'role': request.session['role']})

    def post(self, request):
        form = SignInForm(request.POST)
        if form.is_valid():
            try:
                user, role = AuthService.sign_in(
                    form.data['email'], form.data['password'])
                if user is not None:
                    request.session['role'] = role
                    request.session['user'] = user.email
                    request.session.modified = True
                    return redirect('main')
                form.add_error(None, 'Wrong email or password!')
            except:
                form.add_error(None, 'Sign In error!')
        return render(request, 'auth.html', {'form': form, 'type': 'In', 'role': request.session['role']})


class LogOutView(View):
    def get(self, request):
        request.session.clear()
        check_session(request.session)
        return redirect('main')