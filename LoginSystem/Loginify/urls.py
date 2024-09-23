from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.home_view, name='hello'),  # URL for home view
]