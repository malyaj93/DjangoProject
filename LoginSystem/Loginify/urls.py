from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.home_view, name='hello'),  # URL for hello world view
    path('signup/', views.signup_view, name='signup'),  # URL for signup view
    path('login/', views.login_view, name='login'), # URL for login view
    path('get_all_users/', views.get_all_users, name='get_all_users'),  # URL to fetch all the users
    path('get_user_by_email/<str:email>/', views.get_user_by_email, name='get_user_by_email'),  # URL to fetch user by email
    path('update_user/<str:email>/', views.update_user, name='update_user'),    # URL to update user details
    path('update_partial_user/<str:username>/', views.update_partial_user, name='update_partial_user'), # URL to update partial details of a user
    path('delete_user/<str:username>/', views.delete_user, name='delete_user'), # URL to delete a user
]