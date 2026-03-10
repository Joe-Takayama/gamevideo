from django.urls import path
from .views import SignupView, LoginView, LogoutView, IndexView

app_name = "gamesvideo"

urlpatterns = [
    # 新規登録画面
    path("signup/", SignupView.as_view(), name="signup"),

    # ログイン画面
    path("login/", LoginView.as_view(), name="login"),

    # ログアウト
    path("logout/", LogoutView.as_view(), name="logout"),
    # トップページ
    path("", IndexView.as_view(), name="index"),
    # path("info/", InfoView.as_view(), name="info"),
]
