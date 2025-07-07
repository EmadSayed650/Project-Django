from django.urls import path
from . import views
from django.shortcuts import redirect
from .views import login_view, logout_view, dashboard_view, create_employee_view
urlpatterns = [
    path('', lambda request: redirect('login')),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('create-employee/', create_employee_view, name='create_employee'),
]
