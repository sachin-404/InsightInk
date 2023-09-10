from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('login', views.login_view, name="login_view"),
    path('signup', views.signup_view, name="signup_view"),
]