# courses/models.py
from django.db import models



class Module(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Модуль"
        verbose_name_plural = "Модули"


        
class Lesson(models.Model):
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    video_file = models.FileField("Видео", upload_to='video/', blank=True, null=True)
    image = models.ImageField(upload_to="lessons/", blank=True, null=True)
    content = models.TextField()
    next_lesson = models.ForeignKey('self', on_delete=models.SET_NULL, 
                                  blank=True, null=True,
                                  related_name='previous_lessons')
    
    def __str__(self):
        return f"{self.title} (Модуль: {self.module.title})"

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'

class Material(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='materials')
    title = models.CharField("Название материала", max_length=255)
    description = models.TextField("Описание")
    image = models.ImageField("Изображение", upload_to='media/lessons/', null=True, blank=True)
    order = models.PositiveIntegerField(default=0)
    def __str__(self):
        return self.title

    class Meta:
        ordering = ['order']
        verbose_name = 'Материал'
        verbose_name_plural = 'Материалы'

    def __str__(self):
        return self.title
  

class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'



