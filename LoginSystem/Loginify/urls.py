from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.home_view, name='hello'),  # URL for hello world view
    path('signup/', views.signup_view, name='signup'),  # URL for signup view
    path('login/', views.login_view, name='login'), # URL for login view
]