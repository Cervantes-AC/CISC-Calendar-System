from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from django.contrib.auth.decorators import login_required

def signup_view(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("dashboard")
    else:
        form = CustomUserCreationForm()
    return render(request, "accounts/signup.html", {"form": form})

def login_view(request):
    if request.method == "POST":
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("dashboard")
    else:
        form = CustomAuthenticationForm()
    return render(request, "accounts/login.html", {"form": form})

@login_required
def dashboard(request):
    if request.user.role == "student":
        return render(request, "accounts/student_dashboard.html")
    elif request.user.role == "faculty":
        return render(request, "accounts/faculty_dashboard.html")
    elif request.user.role == "admin":
        return render(request, "accounts/admin_dashboard.html")
    else:
        return redirect("login")

def logout_view(request):
    logout(request)
    return redirect("login")
