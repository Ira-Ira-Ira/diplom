from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.http import HttpResponseRedirect
from .forms import UserLoginForm, UserRegistrationForm
from django.contrib import messages
from .forms import ReviewForm
from .models import UserProgress, Lesson
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm
from .models import Exam, Question, Answer, ExamResult
from django.core.mail import send_mail
from django.conf import settings
from django.utils import timezone
from .forms import AvatarUploadForm

@login_required
def profile_view(request):
    return render(request, 'users/profile.html', {'user': request.user})

@login_required
def upload_avatar(request):
    if request.method == 'POST':
        form = AvatarUploadForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('users:profile')
    else:
        form = AvatarUploadForm(instance=request.user)

    return render(request, 'users/upload_avatar.html', {'form': form})

def exam_view(request, exam_id):
    exam = get_object_or_404(Exam, pk=exam_id)

    if request.method == "POST":
        score = 0
        total_questions = exam.question_set.count()

        for question in exam.question_set.all():
            selected_answer = request.POST.get(f"question_{question.id}")
            if selected_answer:
                answer = Answer.objects.get(pk=selected_answer)
                if answer.is_correct:
                    score += 1

        percentage = int((score / total_questions) * 100)
        passed = percentage >= exam.passing_score

        # Сохраняем результат
        ExamResult.objects.create(
            user=request.user, exam=exam, score=percentage, passed=passed
        )

        if passed:
            # Отправляем email с уведомлением
            send_mail(
                "Курс успешно завершен",
                f'Поздравляем! Вы успешно прошли экзамен по курсу "{exam.course.title}" с результатом {percentage}%. Ваш сертификат будет отправлен в течение 3 рабочих дней.',
                settings.DEFAULT_FROM_EMAIL,
                [request.user.email],
                fail_silently=True,
            )
            return render(
                request, "users/exam_success.html", {"exam": exam, "score": percentage}
            )
        else:
            messages.error(
                request,
                f"Вы набрали {percentage}%. Для успешного прохождения нужно {exam.passing_score}%. Попробуйте еще раз!",
            )
            return redirect("exam", exam_id=exam.id)

    questions = exam.question_set.order_by("order")
    return render(request, "users/exam.html", {"exam": exam, "questions": questions})


def login_user(request):

    if request.user.is_authenticated:
        return redirect("users:profile")

    if request.method == "POST":
        login_form = UserLoginForm(data=request.POST)
        if login_form.is_valid():
            username = request.POST["username"]
            password = request.POST["password"]
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return HttpResponseRedirect(reverse("users:profile"))

        context = {
            "login_form": login_form,
        }
        return render(request, "users/login.html", context)

    else:
        login_form = UserLoginForm()
        context = {
            "login_form": login_form,
        }
        return render(request, "users/login.html", context)


def signup_user(request):

    if request.user.is_authenticated:
        return redirect("users:profile")

    if request.method == "POST":
        registration_form = UserRegistrationForm(data=request.POST)
        if registration_form.is_valid():
            user = registration_form.save()
            login(request, user)
            return redirect("users:profile")

        context = {
            "registration_form": registration_form,
        }
        return render(request, "users/signup.html", context)

    else:
        registration_form = UserRegistrationForm()
        context = {
            "registration_form": registration_form,
        }
        return render(request, "users/signup.html", context)


@login_required
def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse("main:index"))


@login_required(login_url="login/")
def profile(request):
    return render(request, "users/profile.html")


@login_required
def create_review(request):
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.author = request.user
            review.save()
            messages.success(request, "Ваш отзыв успешно отправлен!")
            return redirect("users:profile")
    else:
        form = ReviewForm()

    return render(request, "users/profile.html", {"form": form})


def exam_view(request):
    # Получаем единственный экзамен (первый в базе)
    exam = Exam.objects.first()

    if not exam:
        return render(request, "users/no_exam.html")  # Создайте этот шаблон, если нужно

    if request.method == "POST":
        # Обработка результатов экзамена
        score = 0
        total_questions = exam.question_set.count()

        for question in exam.question_set.all():
            selected_answer = request.POST.get(f"question_{question.id}")
            if selected_answer:
                answer = question.answer_set.get(pk=selected_answer)
                if answer.is_correct:
                    score += 1

        percentage = int((score / total_questions) * 100)
        passed = percentage >= exam.passing_score

        # Сохраняем результат (если у вас есть модель ExamResult)
        if hasattr(request.user, "examresult_set"):
            request.user.examresult_set.create(
                exam=exam, score=percentage, passed=passed
            )

        if passed:
            return render(
                request, "users/exam_success.html", {"exam": exam, "score": percentage}
            )
        else:
            return render(
                request,
                "users/exam_fail.html",
                {
                    "exam": exam,
                    "score": percentage,
                    "passing_score": exam.passing_score,
                },
            )

    questions = exam.question_set.order_by("order")
    return render(request, "users/exam.html", {"exam": exam, "questions": questions})
