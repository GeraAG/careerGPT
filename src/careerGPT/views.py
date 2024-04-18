from django.shortcuts import render
from django.contrib.auth.models import User

def home_view(request):
    return render(request, "pages/home.html", {})

def signup_view(request):
    first_name = request.POST["first_name"]
    last_name = request.POST["last_name"]
    email = request.POST["email"]
    password = request.POST["password"]
    user = User.objects.create_user(username=email, email=email, password=password, first_name=first_name, last_name=last_name)
    user.save()
