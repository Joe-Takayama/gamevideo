from django.urls import path
from .views import SignupView, IndexView

app_name = "gamesvideo"

urlpatterns = [
    path("signup/", SignupView.as_view(), name="signup"),
    path("index/", IndexView.as_view(), name="index"),
    # path("info/", InfoView.as_view(), name="info"),
]
