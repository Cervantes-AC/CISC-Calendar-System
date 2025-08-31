from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm

# ---------------------------
# Registration
# ---------------------------
def register_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully!")
            return redirect('users:login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

# ---------------------------
# Login
# ---------------------------
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('users:dashboard_view')  # fixed namespace to 'users'
        else:
            messages.error(request, "Invalid username or password")
    return render(request, 'users/login.html')

# ---------------------------
# Logout
# ---------------------------
def logout_view(request):
    logout(request)
    return redirect('users:login')

# ---------------------------
# Dashboard
# ---------------------------
@login_required
def dashboard_view(request):
    """Redirect users to dashboard based on role"""
    role = getattr(request.user, 'role', '').lower()  # normalize to lowercase
    if role == 'student':
        return redirect('users:student_dashboard')
    elif role == 'faculty':
        return redirect('users:faculty_dashboard')
    elif role == 'admin':
        return redirect('users:admin_dashboard')
    else:
        messages.error(request, "Role not recognized")
        return redirect('users:login')

@login_required
def student_dashboard(request):
    return render(request, 'users/student_dashboard.html')

@login_required
def faculty_dashboard(request):
    return render(request, 'users/faculty_dashboard.html')

@login_required
def admin_dashboard(request):
    return render(request, 'users/admin_dashboard.html')
