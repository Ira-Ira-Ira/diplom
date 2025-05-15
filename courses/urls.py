# courses/urls.py
from django.urls import path
from . import views


urlpatterns = [
    path('', views.module_list, name='module_list'),

    path('lesson/<int:pk>/', views.lesson_detail, name='lesson_detail'),
    path('lesson/<int:pk>/complete/', views.complete_lesson, name='complete_lesson'),

]
