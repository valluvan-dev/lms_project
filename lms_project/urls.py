"""
URL configuration for lms_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from accounts import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.login_view, name='login'),
    path('create-student/', views.create_student_account, name='create_student'),
    path('create-trainer/', views.create_trainer_account, name='create_trainer'),
    path('create-staff/', views.create_staff_account, name='create_staff'),
    path('success/', views.success, name='success'),
    path('student-dashboard/', views.student_dashboard, name='student_dashboard'),
    path('trainer-dashboard/', views.trainer_dashboard, name='trainer_dashboard'),
    path('staff-dashboard/', views.staff_dashboard, name='staff_dashboard'),
    path('admin-panel/', views.admin_panel, name='admin_panel'),
    path('manage-users/', views.manage_users, name='manage_users'),
    path('create-user/<str:role>/', views.create_user, name='create_user'),
    path('update-user/<int:user_id>/', views.update_user, name='update_user'),
    path('delete-user/<int:user_id>/', views.delete_user, name='delete_user'),
    path('restrict-user/<int:user_id>/', views.restrict_user, name='restrict_user'),
]


