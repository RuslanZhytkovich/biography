from .models import Review
from django import forms
from django.forms import ModelForm

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['author','review']
        widgets = {
            'author': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Имя автора'}),
            'review': forms.Textarea(attrs={'class': 'form-control','placeholder':'Содержание отзыва','cols':60, 'rows': 10}),
        }


