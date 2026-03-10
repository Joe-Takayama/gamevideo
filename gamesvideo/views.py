from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.views import View
from django.contrib.auth import login
from .forms import SignupForm
from django.contrib.auth.decorators import login_required

# 新規登録ビュー
class SignupView(View):
    def get(self, request):
        form = SignupForm()
        return render(request, "signup/signup.html", {"form": form})
    
    def post(self, request):
        form = SignupForm(request.POST)

        if form.is_valid():

          user = form.save()
          login(request, user)
          return redirect("gamesvideo:index")
        return render(request, "signup/signup.html", {"form": form})
    
# ログインビュー
class LoginView(View):
    def get(self, request):
        form = AuthenticationForm()
        return render(request, "login/login.html", {"form": form})
    
    def post(self, request):
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("gamesvideo:index")
        return render(request, "login/login.html", {"form": form})
    
# ログアウトビュー
class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect("gamesvideo:index")
    
# トップ画面ビュー
class IndexView(View):
    def get(self, request):
        return render(request, "gamesvideo/index.html")

# @login_required
# class InfoView(View):
#     def get(self, request):
#         return render(request, "gamesvideo/info.html")
