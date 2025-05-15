from django import forms
from .models import Feedback

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ["name", "email", "phone", "message"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Введите ваше имя"}),
            "email": forms.EmailInput(attrs={"class": "form-control", "placeholder": "Введите ваш email"}),
            "phone": forms.TextInput(attrs={"class": "form-control", "placeholder": "Введите ваш телефон"}),
            "message": forms.Textarea(attrs={"class": "form-control", "placeholder": "Введите ваше сообщение", "rows": 5}),
        }

