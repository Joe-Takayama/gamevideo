from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class SignupForm(UserCreationForm):
    email = forms.EmailField(
        label="",
        widget=forms.EmailInput(attrs={
            "placeholder": "メールアドレスを入力してください"
        })
    )

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
        widgets = {
            "username": forms.TextInput(attrs={
                "placeholder": "ユーザー名を入力してください"
            }),
            "password1": forms.PasswordInput(attrs={
                "placeholder": "パスワードを入力してください"
            }),
            "password2": forms.PasswordInput(attrs={
                "placeholder": "パスワードを再入力してください"
            })
        }