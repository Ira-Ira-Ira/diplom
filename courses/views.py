# courses/views.py
from django.shortcuts import render, get_object_or_404
from .models import Module, Lesson
from users.models import UserProgress
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.utils import timezone


def module_list(request):
    courses = Module.objects.all()
    return render(request, 'courses/module_list.html', {'courses': courses})


def lesson_detail(request, pk):  # Используем pk вместо lesson_id
    lesson = get_object_or_404(Lesson, pk=pk)
    
    # Получаем прогресс пользователя
    progress = None
    is_completed = False
    completed_at = None
    
    if request.user.is_authenticated:
        try:
            user_progress = UserProgress.objects.get(user=request.user, lesson=lesson)
            is_completed = user_progress.completed
            completed_at = user_progress.completed_at
        except UserProgress.DoesNotExist:
            pass
        
        # Рассчитываем общий прогресс
        completed_count = UserProgress.objects.filter(user=request.user, completed=True).count()
        total_count = Lesson.objects.count()
        progress = {
            'completed_count': completed_count,
            'total_count': total_count,
            'percent': int((completed_count / total_count) * 100) if total_count > 0 else 0
        }
    
    return render(request, 'courses/lesson_detail.html', {
        'lesson': lesson,
        'progress': progress,
        'is_completed': is_completed,
        'completed_at': completed_at
    })

def complete_lesson(request, pk):  # Также используем pk здесь
    if not request.user.is_authenticated:
        return redirect('login')
    
    lesson = get_object_or_404(Lesson, pk=pk)
    progress, created = UserProgress.objects.update_or_create(
        user=request.user,
        lesson=lesson,
        defaults={'completed': True, 'completed_at': timezone.now()}
    )
    
    return redirect('lesson_detail', pk=lesson.pk)