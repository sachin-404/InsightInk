from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('login', views.login_view, name="login_view"),
    path('signup', views.signup_view, name="signup_view"),
    path('add-blog', views.add_blog, name="add_blog"),
    path('blog-detail/<slug>', views.blog_detail, name="blog_detail"),
]