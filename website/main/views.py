from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import News
from .forms import ReviewForm

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

def reviews(request):
    data = {
        'title' : 'Отзывы'
    }
    return render(request, 'main/html/reviews.html',data)

def skills(request):
    data = {
        'title': 'Навыки'
    }
    return render(request,'main/html/skills.html',data)

def create(request):
    error = ''
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма была неверной'

    form = ReviewForm()

    data = {
        'form': form,
        'error': error,
    }

    return render(request, 'main/html/create.html',data)