from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'main/html/index.html')

def about(request):
    return render(request, 'main/html/about.html')

def contact(request):
    return HttpResponse('<h1>Contact information</h1>')