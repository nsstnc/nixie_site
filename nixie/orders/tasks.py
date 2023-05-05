from django.core.mail import send_mail
from .models import Order
from huey import crontab
from huey.contrib.djhuey import task

import time
from yoomoney import Client

token = "4100111332784360.F307CA3C81477967BE3602BF778A5FB84DB5AF5476948F2B743D7DFF79D91FBC5348AADC8EC719EF15F1CDC45D4970EB9C35871C55C3B8895A3AA64F9FDF67CB90486981C8EAF038F1653AAD781238BD1F48348828B073315297086A4F8251A386C41BDF9C548070C1EB636F25747229985F1703B67BFCF46C27A3871603E8A5"
client = Client(token)


@task()
def check_pay(order_id, label, pay_url, price):
    order = Order.objects.get(id=order_id)
    # отправка email
    subject = "Ваш заказ оформлен"
    message = 'Здравствуйте {},\n\n Благодарим Вас за размещение заказа на нашем сайте.\
                    Номер заказа {}.\
              \nСумма заказа: {} руб.\
              \n\n Если Вы еще не оплатили свой заказ, пожалуйста, перейдите по ссылке:\
              \n{}'.format(order.first_name, order.id, price, pay_url)
    send_mail(subject, message,
              'nsstnc-service@mail.ru',
              [order.email])
    # проверяем оплату через 2 минуты, 10 минут, час
    for x in [120, 600, 3600]:
        time.sleep(x)
        history = client.operation_history(label=label).operations

        for operation in history:
            if operation.status == "success":
                order.paid = True
                order.save()
                return
