from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.connect, name='Contact'),
    path('success/', views.success, name='Success'),
]
