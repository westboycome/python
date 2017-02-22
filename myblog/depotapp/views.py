from django.shortcuts import render
from django.http import HttpResponse

def product(request):
    return HttpResponse('hello')
