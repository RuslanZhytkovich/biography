
from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('',views.index, name = 'home'),
    path('bio/',views.bio, name = 'bio'),
    path('hobbies/',views.hobbies, name = 'hobbies'),
    path('skills/', views.skills, name='skills'),
    path('reviews/', views.reviews, name = 'reviews'),
    path('reviews/create', views.create, name='create'),
]
