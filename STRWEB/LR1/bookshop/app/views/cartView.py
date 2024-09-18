from django.shortcuts import redirect, render
from django.contrib import messages
from django.views import View
from app.core.validators import check_response
from app.services.cartService import CartService


class CartView(View):
    template_name = 'cart.html'

    def get(self, request):
        role = request.session.get('role')
        cart = CartService.form_cart(request.session.get('cart'))
        if role != 'usr':
            redirect('main')
        return render(request, self.template_name, {'role': role, 'cart': cart})

    def post(self, request):
        email = request.session.get('user')
        role = request.session.get('role')
        if check_response(email, request) or role != 'usr':
            return redirect('main')
        if 'del' in request.POST.get('action'):
            book_id = request.POST['action'].split('_')[1]
            cart: list = request.session.get('cart')
            if cart is not None:
                cart.reverse()
                cart.remove(book_id)
                cart.reverse()
            request.session['cart'] = cart
            request.session.save()
        elif 'add' in request.POST.get('action'):
            book_id = request.POST['action'].split('_')[1]
            cart: list | None = CartService.count_book(
                request.session.get('cart'), book_id)
            if cart is None:
                messages.error(request, "Not enough books in catalog!")
                return render(request, self.template_name, {'role': role,
                                                            'cart': CartService.form_cart(request.session.get('cart'))})
            cart.append(book_id)
            request.session['cart'] = cart
            request.session.save()

        return redirect('cart')
