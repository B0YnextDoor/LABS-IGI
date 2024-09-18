from django.shortcuts import render
from django.views import View


class SandBoxView(View):
    template_name = 'sandbox.html'

    def get(self, request):
        return render(request, self.template_name, {'role': request.session['role'], 'cart': request.session['cart']})

    def post(self, request):
        data = dict()
        action = request.POST.get('action')
        if (action == "form1"):
            data['username'] = request.POST['username']
            data['email'] = request.POST['email']
            data['password'] = request.POST['password']
            data['birthdate'] = request.POST['birthdate']
            return render(request, self.template_name, {'role': request.session['role'],
                                                        'cart': request.session['cart'], 'form1': data})
        elif (action == "form2"):
            data['photo'] = request.FILES['photo']
            data['age'] = request.POST['age']
            data['gender'] = request.POST['gender']
            data['color'] = request.POST['color']
            data['interest'] = request.POST.getlist('interest')
            return render(request, self.template_name, {'role': request.session['role'],
                                                        'cart': request.session['cart'], 'form2': data})
        data['phone'] = request.POST['phone']
        data['subject'] = request.POST['subject']
        data['message'] = request.POST['message']
        return render(request, self.template_name, {'role': request.session['role'],
                                                    'cart': request.session['cart'], 'form3': data})
