from django.urls import path
from . import views
#  . means current folder


# /products
# /products/1/detail
# about

urlpatterns = [
    path('', views.index),
    path('new', views.new)
]