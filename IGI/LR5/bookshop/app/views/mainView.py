from django.shortcuts import render
from app.core.validators import check_session
from app.services.apiService import ApiService


def index(request):
    check_session(request.session)
    return render(request, 'main.html', {'role': request.session['role']})


def policy(request):
    check_session(request.session)
    fact, joke = ApiService.request_to_api()
    return render(request, 'policy.html', {'fact': fact, 'joke': joke, 'role': request.session['role']})
