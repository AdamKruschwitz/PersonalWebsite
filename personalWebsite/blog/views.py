from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from .models import Article

class IndexView(generic.ListView):
    template_name = 'blog/index.html'
    context_object_name = 'articles'

    def get_queryset(self):
        """
        Return the latest articles that have a publication date less than or
        equal to now in order of their publication date descending
        """
        return Article.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:20]

class ArticleView(generic.DetailView):
    model = Article
    template_name = 'blog/article.html'

    def get_queryset(self):
        """
        Return articles that have a publication date less than or equal to now
        """
        return Article.objects.filter(pub_date__lte=timezone.now())
