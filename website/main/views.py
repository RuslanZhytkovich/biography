from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'main/html/index.html', {'title':'Главная страница'})

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