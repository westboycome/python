from django.shortcuts import render
from django.http import HttpResponse
from . import models

def index(request):
    articles = models.Article.objects.all()
    return render(request, 'index.html', {'articles': articles})

def edit_page(request):
    pass