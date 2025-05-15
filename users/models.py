from django.db import models
from django.contrib.auth.models import AbstractUser
from courses.models import Lesson

class User(AbstractUser):
    avatar = models.ImageField(upload_to='avatars/', default='avatars/default.png')
    
    def get_progress(self):
        total_lessons = Lesson.objects.count()
        completed_lessons = self.userlessonprogress_set.filter(completed=True).count()
        percent = 0
        if total_lessons > 0:
            percent = round((completed_lessons / total_lessons) * 100)
        
        return {
            'total': total_lessons,
            'completed': completed_lessons,
            'percent': percent
        }
    
        last_completed = self.userprogress_set.filter(completed=True).order_by('-completed_at').first()
    
        return {
        # ... предыдущие данные ...
        'last_completed_lesson': last_completed.lesson if last_completed else None,
        'last_completed_date': last_completed.completed_at if last_completed else None
        }

class UserProgress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='completed_lessons')
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
    completed_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        unique_together = ('user', 'lesson')
        verbose_name_plural = 'User Progress'




class Exam(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    passing_score = models.PositiveIntegerField(default=70)
    course = models.ForeignKey('courses.Course', on_delete=models.CASCADE, related_name='exams')
    
    def __str__(self):
        return f"{self.title} (Курс: {self.course.title})"

class Question(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    text = models.TextField()
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.text

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.text

class ExamResult(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    score = models.PositiveIntegerField()
    passed = models.BooleanField(default=False)
    completed_at = models.DateTimeField(auto_now_add=True)

