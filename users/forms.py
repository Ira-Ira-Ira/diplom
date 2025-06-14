from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from users.models import User
from main.models import Review



class AvatarUploadForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['avatar']
        
class UserLoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={"autofocus": True,
                                      "placeholder": "Логин"}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"autocomplete": "current-password",
                                          "placeholder" : "Пароль"}),
    )
    class Meta:
        model = User
        fields = ['username', 'password']

class UserRegistrationForm(UserCreationForm):

    email = forms.EmailField(
        label="Электронная почта",
        error_messages={
            'invalid': "Введите корректный адрес электронной почты."
        }
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Пользователь с таким email уже существует.")
        return email


    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Имя"
            }
        )
    )

    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Логин"
            }
        )
    )
    
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "autocomplete": "current-password",
                "placeholder" : "Пароль"
            }
        ),
    )

    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "autocomplete": "current-password",
                "placeholder" : "Повтор пароля"
            }
        ),
    )

    class Meta:
        model = User
        fields = (
            "email",
            "first_name",
            "username",
            "password1",
            "password2",
        )


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['text']


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'avatar', 'password1', 'password2')