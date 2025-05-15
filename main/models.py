from django.db import models
from django.contrib.auth.models import User
from django.conf import settings



class Feedback(models.Model):
    class Meta:
        db_table = 'Feedback'
        verbose_name = 'Обратная связь'
        verbose_name_plural = 'Обратная связь'

    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True, null=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Отзыв от {self.name} ({self.email})"




# Create your models here.
class Review(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Автор")
    text = models.TextField(verbose_name="Текст отзыва")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"

    def str(self):
        return f"Отзыв от {self.author.username}"