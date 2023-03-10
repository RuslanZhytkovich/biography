from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import *
from .forms import ReviewForm
from django.views.generic import DetailView




class NewsDetailView(DetailView):

    model = News
    template_name = 'main/html/details_view.html'
    context_object_name = 'news'








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
    reviews = Review.objects.all()
    return render(request, 'main/html/reviews.html', {'reviews': reviews})

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