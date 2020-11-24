from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from django.urls import reverse
from django.views import generic
from django.utils import timezone

# Create your views here.
def index(request):
    return HttpResponse("Hello world, you're at the contact me index page")

def connect(request):
    return HttpResponse("Hello world, you're at the contact me connect page")

def success(request):
    return HttpResponse("Hello world, you're at the contact me success page")
