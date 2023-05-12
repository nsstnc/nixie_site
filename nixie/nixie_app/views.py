from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import ContactForm, ReviewForm
from django.core.mail import send_mail, BadHeaderError
from django.urls import reverse, reverse_lazy
from django_filters.views import FilterView

from .models import Product, Review
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
    products = Product.objects.filter(available=True)
    f = ProductFilter(request.GET, queryset=products)

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


from pathlib import Path
import os


def portfolio(request):
    cart = Cart(request)
    contact(request)
    form = ContactForm()
    # получаем путь к изображениям
    os.chdir(os.path.join(Path(__file__).resolve().parent.parent, 'nixie_app/templates/nixie_app/images/products'))
    images_names = []
    # получаем имена изображений с расширениями jpg, png, jpeg
    images_names += [each for each in os.listdir(".") if each.endswith(('.png', '.jpg', '.jpeg'))]
    res = {
        "form": form,
        'cart': cart,
        'cart_len': len(cart),
        'images_names': images_names
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
    reviews = Review.objects.filter(available=True)
    res = {
        "form": form,
        'cart': cart,
        'cart_len': len(cart),
        'reviews': reviews
    }
    return render(request, "nixie_app/reviews.html", context=res)


def review_create(request):
    cart = Cart(request)
    contact(request)
    form = ContactForm()
    if request.method == 'POST':
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            review_form.save()
            res = {
                'form': form,
                'cart_len': len(cart),
            }

        return render(request, 'nixie_app/created.html', res)

    else:
        review_form = ReviewForm()
        res = {
            'form': form,
            'cart_len': len(cart),
            'review_form': review_form,
        }
        return render(request, 'nixie_app/create.html', res)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))  # возврат текущей страницы


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
