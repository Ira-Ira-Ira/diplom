from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Feedback
from .forms import FeedbackForm
from .models import Review


def index(request):
    form = FeedbackForm()
    context = {
        'title': 'Цветочные секреты',
        'form': form
    }
    return render(request, 'main/index.html', context)


def about(request):
    context = {
        'title': 'О курсе'
    }
    return render(request, 'main/about.html', context)

def gallery(request):
    context = {
        'title': 'Галерея'
    }
    return render(request, 'main/gallery.html', context)

def contacts(request):
    context = {
        'title': 'Контакты'
    }
    return render(request, 'main/contacts.html', context)

def reviews(request):
    context = {
        'title': 'Отзывы'
    }
    return render(request, 'main/reviews.html', context)

def feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main:index')
    else:
        form = FeedbackForm()

    return render(request, 'main/index.html', {'form': form})


def feedback_success(request):
    return render(request, 'main/feedback_success.html')


def reviews(request):
    latest_reviews = Review.objects.all().order_by('-created_at')[:5]
    context = {
        'title': 'Отзывы',
        'latest_reviews': latest_reviews,
    }
    return render(request, 'main/reviews.html', context)