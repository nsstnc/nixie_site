from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.urls import reverse, reverse_lazy
from django_filters.views import FilterView

from .models import Product
from .filters import ProductFilter

from cart.forms import CartAddProductForm
from cart.cart import Cart


# Create your views here.
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "ВОПРОС ОТ ПОЛЬЗОВАТЕЛЯ"
            body = {
                'name': form.cleaned_data['name'],
                'email': form.cleaned_data['email_address'],
                'message': form.cleaned_data['message'],
            }
            message = "\n".join(body.values())
            # try:
            #     send_mail(subject, message,
            #               'admin@example.com',
            #               ['admin@example.com'])
            try:
                send_mail(subject, message,
                          'nsstnc-service@mail.ru',
                          ['egorgolubev0484@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Форма заполнена неверно')
            return redirect("main-name")


def product_detail(request, id, slug):
    cart = Cart(request)
    form = ContactForm()
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    cart_product_form = CartAddProductForm()
    res = {
        "form": form,
        'product': product,
        'cart_product_form': cart_product_form,
        'cart': cart,
        'cart_len': len(cart),
    }
    return render(request, 'nixie_app/detail.html', res)


def main(request):
    cart = Cart(request)
    contact(request)
    form = ContactForm()
    products = Product.objects.order_by("-price")
    cart_product_form = CartAddProductForm()
    res = {
        "form": form,
        'cart': cart,
        'cart_len': len(cart),
        'products': products,
        'cart_product_form': cart_product_form,
    }
    return render(request, "nixie_app/main.html", context=res)


def catalog(request):
    cart = Cart(request)
    contact(request)
    form = ContactForm()
    cart_product_form = CartAddProductForm()
    f = ProductFilter(request.GET, queryset=Product.objects.all())
    products = Product.objects.filter(available=True)

    current_filters = []
    try:
        current_filters.append(request.GET['ordering'])
        current_filters.append(request.GET['lamp_currency'])
        current_filters.append(request.GET['lamp_type'])
        current_filters.append(request.GET['material'])
    except:
        ...
    has_filter = any(filt != '' for filt in current_filters)

    res = {
        "form": form,
        "products": products,
        "filter": f,
        'current_filters': current_filters,
        'has_filter': has_filter,
        'cart_product_form': cart_product_form,
        'cart': cart,
        'cart_len': len(cart),
    }

    return render(request, "nixie_app/catalog.html", context=res)


def portfolio(request):
    cart = Cart(request)
    contact(request)
    form = ContactForm()
    res = {
        "form": form,
        'cart': cart,
        'cart_len': len(cart),
    }
    return render(request, "nixie_app/portfolio.html", context=res)


def delivery(request):
    cart = Cart(request)
    contact(request)
    form = ContactForm()
    res = {
        "form": form,
        'cart': cart,
        'cart_len': len(cart),
    }
    return render(request, "nixie_app/delivery.html", context=res)


def reviews(request):
    cart = Cart(request)
    contact(request)
    form = ContactForm()
    res = {
        "form": form,
        'cart': cart,
        'cart_len': len(cart),
    }
    return render(request, "nixie_app/reviews.html", context=res)


def questions(request):
    cart = Cart(request)
    contact(request)
    form = ContactForm()
    res = {
        "form": form,
        'cart': cart,
        'cart_len': len(cart),
    }
    return render(request, "nixie_app/questions.html", context=res)


def basket(request):
    cart = Cart(request)
    contact(request)
    form = ContactForm()

    res = {
        "form": form,
        'cart': cart,
        'cart_len': len(cart),
    }
    return render(request, "nixie_app/basket.html", context=res)


def info(request):
    cart = Cart(request)
    contact(request)
    form = ContactForm()
    res = {
        "form": form,
        'cart': cart,
        'cart_len': len(cart),
    }
    return render(request, "nixie_app/info.html", context=res)
