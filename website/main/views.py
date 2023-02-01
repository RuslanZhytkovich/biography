from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'main/html/index.html')

def bio(request):
    return render(request, 'main/html/bio.html')

def hobbies(request):
    return render(request,'main/html/hobbies.html')

def skills(request):
    return render(request,'main/html/skills.html')