from django.shortcuts import render
from app.core.validators import check_session
from app.services.apiService import ApiService
from app.services.commonService import NewsService, PartnerService
from django.http import JsonResponse


def index(request):
    check_session(request.session)
    news = NewsService.get_all()
    return render(request, 'main.html', {'role': request.session['role'], 'n': None if len(news) == 0 else news[0],
                                         'partners': PartnerService.get_all(), 'cart': request.session.get('cart')})


def cubeCalculator(request):
    return render(request, 'cubes.html', {'role': request.session['role'], 'cart': request.session['cart']})


def policy(request):
    check_session(request.session)
    fact, joke = ApiService.request_to_api()
    return render(request, 'policy.html', {'fact': fact, 'joke': joke, 'role': request.session['role'],
                                           'cart': request.session.get('cart')})
