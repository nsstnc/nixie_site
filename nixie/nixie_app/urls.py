from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main-name'),
    path('portfolio/', views.portfolio, name='portfolio-name'),
    path('catalog/', views.catalog, name='catalog-name'),
    path('catalog/<id>/<slug>', views.product_detail, name='product-detail'),
    path('info/', views.info, name='info-name'),
    path('delivery/', views.delivery, name='delivery-name'),
    path('reviews/', views.reviews, name='reviews-name'),
    path('reviews/create', views.review_create, name='reviews-create'),
    path('questions/', views.questions, name='questions-name')
]
