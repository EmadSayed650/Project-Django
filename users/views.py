# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import EmployeeCreationForm
from .models import CustomUser  # تأكد إنك مستورد CustomUser


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'users/login.html')

@login_required
def dashboard_view(request):
    if request.user.role == 'manager':
        return render(request, 'users/manager_dashboard.html')
    else:
        return render(request, 'users/employee_dashboard.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

# users/views.py


@login_required
def create_employee_view(request):
    if request.user.role != 'manager':
        messages.error(request, "You are not authorized to create employees.")
        return redirect('dashboard')

    if request.method == 'POST':
        form = EmployeeCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Employee account created successfully!")
            return redirect('dashboard')
    else:
        form = EmployeeCreationForm()

    return render(request, 'users/create_employee.html', {'form': form})



@login_required
def view_employees(request):
    if request.user.role != 'manager':
        return render(request, 'users/unauthorized.html')  # لو مش مدير يظهر صفحة رفض

    employees = CustomUser.objects.filter(role='employee')
    return render(request, 'users/view_employees.html', {'employees': employees})

