from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import UserDetails

# Create your views here.
def home_view(request):
    return HttpResponse("Hello, world!")


# View logic for signup
def signup_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        # Checking if email already exists
        if UserDetails.objects.filter(email=email).exists():
            return HttpResponse("Email already exists!")
        else:
            # Creating a new user and save the changes to DB
            user = UserDetails(username=username, email=email, password=password)
            user.save()
            # Redirect to login page after creating a new user
            return redirect('login')
    return render(request, 'Loginify\signup.html')


# View logic for login
def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        # Check if the entered details are correct or not
        try:
            # if details are correct display the message with the username
            user = UserDetails.objects.get(email=email, password=password)
            return HttpResponse(f"Welcome to the application, {user.username}!")
        except UserDetails.DoesNotExist:
            # if details are incorrect throw error
            return HttpResponse("Invalid email or password!")
    return render(request, 'Loginify\login.html')