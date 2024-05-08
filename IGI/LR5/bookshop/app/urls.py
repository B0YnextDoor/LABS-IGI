from django.urls import path, re_path
from app.views import authView, mainView, infoView, bookView, \
    accountView, newsView, orderView, saleView, adminView, qaView, \
    vacancyView, reviewView, contactView

urlpatterns = [
    path('', mainView.index, name="main"),

    # auth
    path('sign-up/', authView.SignUpView.as_view(), name='signup'),
    path('sign-in/', authView.SignInView.as_view(), name='signin'),
    path('log-out/', authView.LogOutView.as_view(), name='log-out'),

    # account
    path('lk/', accountView.AccountView.as_view(), name='account'),

    # admin
    path('admin-pannel/', adminView.AdminView.as_view(), name='admin'),

    # orders
    path('orders/', orderView.OrderView.as_view(), name='order'),
    re_path(r'^orders/(?P<id>\d+)$',
            orderView.OrderDetailView.as_view(), name='order-detail'),

    # books catalog
    path('books/', bookView.BookView.as_view(), name='catalog'),
    re_path(r'^books/(?P<id>\d+)$',
            bookView.BookDetailView.as_view(), name='book-detail'),

    # about
    path('about/', infoView.InfoView.as_view(), name='about'),

    # news
    path('news/', newsView.NewsView.as_view(), name='news'),
    re_path(r'^news/(?P<id>\d+)$',
            newsView.NewsDetailView.as_view(), name='news-detail'),

    # faq
    path('faq/', qaView.QAView.as_view(), name='faq'),

    # contacts
    path('contacts/', contactView.EmployeeInfoView.as_view(), name='contacts'),

    # vacancies
    path('vacancies/', vacancyView.VacancyView.as_view(), name='vacancies'),

    # reviews
    path('reviews/', reviewView.ReviewView.as_view(), name='reviews'),

    # sale codes
    path('sales/', saleView.SaleCodeView.as_view(), name='sale'),

    # privacy policy
    path('policy/', mainView.policy, name='policy')
]
