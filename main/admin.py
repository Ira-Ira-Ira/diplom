from django.contrib import admin
from .models import Feedback
from .models import Review


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'message', 'created_at')
    search_fields = ('name', 'email', 'phone')




admin.site.register(Review)