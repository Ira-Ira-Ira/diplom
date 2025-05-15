from django.contrib import admin


from .models import User, UserProgress, Exam, Question, Answer, ExamResult

admin.site.register(User)
admin.site.register(UserProgress)
admin.site.register(Exam)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(ExamResult)