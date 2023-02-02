from django.http import HttpResponse
from django.shortcuts import render
from.models import News

def index(request):
    news = News.objects.all()
    return render(request, 'main/html/index.html', {'news': news})

def bio(request):
    data = {
        'title':'Биография'
    }
    return render(request, 'main/html/bio.html', data )

def hobbies(request):
    data = {
        'title': 'Хобби'
    }

    return render(request,'main/html/hobbies.html',data)

def skills(request):
    data = {
        'title': 'Навыки'
    }
    return render(request,'main/html/skills.html',data)