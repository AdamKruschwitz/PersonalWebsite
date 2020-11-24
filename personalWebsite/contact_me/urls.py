from django.urls import path

from . import views

app_name = 'contact_me'

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='Contact'),
    path('success/', views.success, name='Success'),
]
