from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import login
from .forms import SignupForm

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
    
class IndexView(View):
    def get(self, request):
        return render(request, "gamesvideo/index.html")
