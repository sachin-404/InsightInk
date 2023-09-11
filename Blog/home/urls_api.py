from django.urls import path, include
from . import views_api

urlpatterns = [
    path('login/', views_api.LoginView),
    path('signup/', views_api.SignupView),
]