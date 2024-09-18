from django.http import Http404
from django import forms
from django.shortcuts import render, redirect
from django.views import View
from app.app_models.bookModels import Book
from app.services.bookService import BookService
from app.core.validators import number_validator


class BookDetailForm(forms.ModelForm):
    def clean(self):
        number_validator(self.cleaned_data['price'], float, self)
        number_validator(self.cleaned_data['amount'], int, self)
        return self.cleaned_data

    class Meta:
        model = Book
        exclude = ['id', 'created_at', 'updated_at']


class BookView(View):
    model = Book
    context_object_name = 'book_list'
    template_name = 'books.html'

    def get_queryset(self, param: str = 'amount'):
        return BookService.get_all(param)

    def get(self, request):
        self.object_list = self.get_queryset()
        if ((request.session['role'] == 'usr' and request.session.get('cart') is None) or
                request.session['role'] != 'usr'):
            request.session['cart'] = []
            request.session.save()
        if (request.GET.get('search')):
            self.object_list = list(filter(
                lambda b: request.GET['search'] in b.title, list(self.object_list)))
        return render(request, self.template_name, {'role': request.session['role'], 'book_list': self.object_list, 'form': None, 'cart': request.session.get('cart')})

    def post(self, request):
        if (request.POST.get('action') is None):
            self.object_list = self.get_queryset(request.POST['sort_by'])
            return render(request, self.template_name, {'role': request.session['role'], 'book_list': self.object_list, 'form': None, 'cart': request.session.get('cart')})
        form = None
        if request.session.get('role') != 'adm':
            return redirect('catalog')
        if (request.POST.get('action') == 'create'):
            return render(request, self.template_name, {'role': request.session['role'],
                                                        'book_list': None,
                                                        'form': BookDetailForm(),
                                                        'cart': request.session.get('cart')})
        form = BookDetailForm(request.POST)
        if form.is_valid():
            try:
                book = BookService.create(form.data['title'], float(form.data['price']),
                                          int(form.data['amount']), int(form.data['genre']), int(form.data['author']))
                if book is not None:
                    return redirect('catalog')
                form.add_error('None', 'Edit error!')
            except:
                form.add_error(None, 'Creation error!')
        return render(request, self.template_name, {'role': request.session['role'],
                                                    'book_list': None, 'form': form,
                                                    'cart': request.session.get('cart')})


class BookDetailView(View):
    model = Book
    context_object_name = 'book'
    template_name = 'book-detail.html'

    def get_book(self, id: int):
        return BookService.get_by_id(id)

    def get(self, request, id):
        book = self.get_book(id)
        if book is None:
            return Http404("Book does not exist")
        return render(request, self.template_name, {'role': request.session['role'], 'book': book, 'form': None,
                                                    'cart': request.session.get('cart')})

    def post(self, request, id):
        if (request.session.get('role') != 'adm'):
            return redirect('catalog')
        if (request.POST.get('action') == 'edit'):
            book = self.get_book(id)
            form = BookDetailForm(
                initial={'title': book.title, 'price': book.price, 'amount': book.amount, 'genre': book.genre, 'author': book.author})
            return render(request, self.template_name, {'role': request.session['role'], 'book': book, 'form': form,
                                                        'cart': request.session.get('cart')})
        elif (request.POST.get('action') == 'del'):
            BookService.delete(int(id))
            return redirect('catalog')
        form = BookDetailForm(request.POST)
        if form.is_valid():
            try:
                book = BookService.update(int(id), form.data['title'], float(form.data['price']),
                                          int(form.data['amount']), int(form.data['genre']), int(form.data['author']))
                if book is None:
                    form.add_error('None', 'Edit error!')
                else:
                    form = None
            except:
                form.add_error('None', 'Edit error!')
        return render(request, self.template_name, {'role': request.session['role'], 'book': self.get_book(id),
                                                    'form': form, 'cart': request.session.get('cart')})
