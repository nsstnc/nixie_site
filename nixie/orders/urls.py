from django.urls import path
from . import views


urlpatterns = [
    path(r'^create/$', views.order_create, name='order_create'),
    path(r'^create/(?P<product_id>\d+)/$', views.order_create_one, name='order_create_one'),
]