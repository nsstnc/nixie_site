from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import OrderItem
from nixie_app.models import Product
from nixie_app.views import contact
from .forms import OrderCreateForm
from cart.cart import Cart
from nixie_app.forms import ContactForm
from yoomoney import Quickpay
from yoomoney import Client
from .tasks import check_pay
import time
import secrets
import string

# client_id = C1CD12AF0A6B9589F6F935AD933B1F0FAAAE77EAD1563D066B42EFFC20FF1B55
token = "4100111332784360.F307CA3C81477967BE3602BF778A5FB84DB5AF5476948F2B743D7DFF79D91FBC5348AADC8EC719EF15F1CDC45D4970EB9C35871C55C3B8895A3AA64F9FDF67CB90486981C8EAF038F1653AAD781238BD1F48348828B073315297086A4F8251A386C41BDF9C548070C1EB636F25747229985F1703B67BFCF46C27A3871603E8A5"
client = Client(token)


def order_create_one(request, product_id):
    form = ContactForm()
    contact(request)
    product = get_object_or_404(Product, id=product_id)
    cart = Cart(request)
    if request.method == 'POST':
        order_form = OrderCreateForm(request.POST)
        if order_form.is_valid():
            order = order_form.save()
            OrderItem.objects.create(order=order,
                                     product=product,
                                     price=product.price,
                                     quantity=1)
            # задаем уникальный тег для заказа
            label = str(''.join(secrets.choice(string.ascii_uppercase + string.ascii_lowercase) for i in range(20)))

            price = product.price
            # формирование объекта класса quickpay для получения ссылки на оплату через юmoney
            quickpay = Quickpay(
                receiver="4100111332784360",
                quickpay_form="shop",
                targets="Sponsor this project",
                paymentType="SB",
                sum=cart.get_total_price() / 10,
                label=order.id)
            pay_url = quickpay.base_url

            res = {'order': order,
                   'form': form,
                   'cart_len': len(cart),
                   'pay_url': pay_url,
                   }
            # запускаем проверку оплаты и отправляем email клиенту
            check_pay(order.id, label, pay_url, price)()

            return render(request, 'orders/order/created.html', res)
    else:

        order_form = OrderCreateForm()

        res = {'item': product,
               'form': form,
               'order_form': order_form,
               'cart_len': len(cart),
               }
        return render(request, 'orders/order/create.html', res)


def order_create(request):
    cart = Cart(request)
    form = ContactForm()
    contact(request)
    if request.method == 'POST':
        order_form = OrderCreateForm(request.POST)
        if order_form.is_valid():
            order = order_form.save()
            for item in cart:
                if item['quantity'] != 0:
                    OrderItem.objects.create(order=order,
                                             product=item['product'],
                                             price=item['price'],
                                             quantity=item['quantity'])

            price = cart.get_total_price()
            # очистка корзины
            cart.clear()

            # задаем уникальный тег для заказа
            label = str(''.join(secrets.choice(string.ascii_uppercase + string.ascii_lowercase) for i in range(20)))

            # формирование объекта класса quickpay для получения ссылки на оплату через юmoney
            quickpay = Quickpay(
                receiver="4100111332784360",
                quickpay_form="shop",
                targets="Sponsor this project",
                paymentType="SB",
                sum=cart.get_total_price() / 10,
                label=label)
            # url для перенаправления после успешной оплаты
            pay_url = quickpay.base_url  # ссылка на оплату

            res = {'order': order,
                   'form': form,
                   'cart_len': len(cart),
                   'pay_url': pay_url,
                   }
            # запускаем проверку оплаты и отправляем email клиенту
            check_pay(order.id, label, pay_url, price)()

        return render(request, 'orders/order/created.html', res)

    else:
        order_form = OrderCreateForm()

    if len(cart) != 0:
        res = {'cart': cart,
               'form': form,
               'order_form': order_form,
               'cart_len': len(cart),
               }
        return render(request, 'orders/order/create.html', res)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))  # возврат текущей страницы
