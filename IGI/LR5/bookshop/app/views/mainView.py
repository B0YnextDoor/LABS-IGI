from django.shortcuts import render
from app.core.validators import check_session
from app.services.apiService import ApiService
from app.services.commonService import NewsService


def index(request):
    check_session(request.session)
    news = NewsService.get_all()
    return render(request, 'main.html', {'role': request.session['role'], 'n': None if len(news) == 0 else news[0]})


def policy(request):
    check_session(request.session)
    fact, joke = ApiService.request_to_api()
    return render(request, 'policy.html', {'fact': fact, 'joke': joke, 'role': request.session['role']})
