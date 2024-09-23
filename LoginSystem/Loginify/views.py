import json

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserDetailsSerializer

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


# View to get all user details
@api_view(['GET'])
def get_all_users(request):
    if request.method == 'GET':
        try:
            all_users = UserDetails.objects.all()
            serializer_data = UserDetailsSerializer(all_users, many=True)
            return JsonResponse(serializer_data.data, safe=False)
        except Exception as e:
            return JsonResponse({"error": str(e)})


# View to get a single user by email
@api_view(['GET'])
def get_user_by_email(request, email):
    if request.method == 'GET':
        try:
            user_by_email = UserDetails.objects.get(email=email)
            serializer_data = UserDetailsSerializer(user_by_email)
            return JsonResponse(serializer_data.data, safe=False)
        except UserDetails.DoesNotExist:
                    return Response({'error': 'User not found'}, status=404)

# View to update a user's details
@api_view(['PUT'])
def update_user(request, email):
    if request.method == 'PUT':
        try:
            user_data = UserDetails.objects.get(email=email)
            input_data= json.loads(request.body)
            serializer_data = UserDetailsSerializer(user_data, data=input_data)
            if serializer_data.is_valid():
                serializer_data.save()
                return JsonResponse({'message': 'User data updated successfully'}, status=200)
            else:
                return JsonResponse(serializer_data.errors, status=400)
        except UserDetails.DoesNotExist:
            return Response({'error': 'User not found'}, status=404)

# View to update a partial user's details
@api_view(['PATCH'])
def update_partial_user(request, username):
    if request.method == 'PATCH':
        try:
            user_data = UserDetails.objects.get(username=username)
            input_data= json.loads(request.body)
            serializer_data = UserDetailsSerializer(user_data, data=input_data, partial=True)
            if serializer_data.is_valid():
                serializer_data.save()
                return JsonResponse({'message': 'User data updated successfully'}, status=200)
            else:
                return JsonResponse(serializer_data.errors, status=400)
        except UserDetails.DoesNotExist:
            return Response({'error': 'User not found'}, status=404)

@api_view(['DELETE'])
def delete_user(request, username):
    if request.method == 'DELETE':
        try:
            user_data = UserDetails.objects.get(username=username)
            user_data.delete()
            return JsonResponse({'message': 'User deleted successfully'}, status=204)
        except UserDetails.DoesNotExist:
            return Response({'error': 'User not found'}, status=404)