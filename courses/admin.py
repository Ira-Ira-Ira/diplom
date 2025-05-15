# courses/admin.py
from django.contrib import admin
from .models import Module, Lesson, Material, Course

admin.site.register(Module)
admin.site.register(Lesson)
admin.site.register(Material)
admin.site.register(Course)

