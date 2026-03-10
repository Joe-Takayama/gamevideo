from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Video
from django import forms

# 新規登録フォーム
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

# 投稿フォーム
class VideoForm(forms.ModelForm):
   title = forms.CharField(
       min_length=3,
       max_length=255,
       widget=forms.TextInput(attrs={"placeholder": "タイトルを入力してください"})
   )

   video = forms.FileField()

   description = forms.CharField(
    required=False,
    min_length=5,
    max_length=255,
    widget=forms.Textarea(attrs={"placeholder": "説明を入力してください"})
   )

   class Meta:
    model = Video
    fields = ("title", "video", "description")