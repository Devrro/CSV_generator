from apps.login.views import UserLoginView
from django.urls import path
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('/login', UserLoginView.as_view(), name="login"),
    path('/logout', LogoutView.as_view(next_page="login"), name="logout"),
]
