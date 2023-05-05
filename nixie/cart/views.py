from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from nixie_app.models import Product
from nixie_app.forms import ContactForm
from .cart import Cart
from .forms import CartAddProductForm
from django.http import HttpResponseRedirect


@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))  # возврат текущей страницы


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    form = ContactForm()
    res = {
        "form": form,
        'cart': cart,
        'cart_len': len(cart),
    }
    return render(request, 'cart/detail.html', res)
