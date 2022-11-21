from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


def home(request):
    return render(request, "accounts/index.html")


def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        if User.objects.filter(username=username):
            messages.error(request, " This username is already taken.")
            return redirect('home')

        if User.objects.filter(email=email):
            messages.error(request, " Email is invalid or already taken.")
            return redirect('home')

        if len(username) > 16:
            messages.error(request, " Username must be under 16 characters.")

        if pass1 != pass2:
            messages.error(request, " Passwords does not match.")

        if not username.isalnum():
            messages.error(request, " Username cannot contain special characters.")
            return redirect('home')

        myuser = User.objects.create_user(username, email, pass1)

        myuser.save()

        messages.success(request, " Your Account has been successfully created.")

        return redirect('signin')

    return render(request, "accounts/signup.html")


def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = authenticate(username=username, password=pass1)

        if user is not None:
            login(request, user)
            username = user.username
            return render(request, "base.html", {'username': username})

        else:
            messages.error(request, " Incorrect username or password. Please try again.")
            return redirect('home')

    return render(request, "accounts/signin.html")


def signout(request):
    logout(request)
    messages.success(request, "Logged Out Successfully.")
    return redirect('home')

# Create your views here.
