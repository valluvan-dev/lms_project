# from django.shortcuts import render, redirect
# from .forms import UserForm, StudentForm, TrainerForm, StaffForm
# from .models import Student, Trainer, Staff

# def create_student_account(request):
#     if request.method == 'POST':
#         user_form = UserForm(request.POST)
#         if user_form.is_valid():
#             user = user_form.save(commit=False)
#             user.set_password(user.password)
#             user.save()
#             Student.objects.create(user=user)
#             return redirect('success')
#     else:
#         user_form = UserForm()
#     return render(request, 'create_account.html', {'form': user_form, 'account_type': 'Student'})

# def create_trainer_account(request):
#     if request.method == 'POST':
#         user_form = UserForm(request.POST)
#         if user_form.is_valid():
#             user = user_form.save(commit=False)
#             user.set_password(user.password)
#             user.save()
#             Trainer.objects.create(user=user)
#             return redirect('success')
#     else:
#         user_form = UserForm()
#     return render(request, 'create_account.html', {'form': user_form, 'account_type': 'Trainer'})

# def create_staff_account(request):
#     if request.method == 'POST':
#         user_form = UserForm(request.POST)
#         if user_form.is_valid():
#             user = user_form.save(commit=False)
#             user.set_password(user.password)
#             user.save()
#             Staff.objects.create(user=user)
#             return redirect('success')
#     else:
#         user_form = UserForm()
#     return render(request, 'create_account.html', {'form': user_form, 'account_type': 'Staff'})


# def success(request):
#     return render(request, 'success.html')



from django.shortcuts import render, redirect,get_object_or_404                                                                                                                                                                                                            ]
from django.contrib.auth import login
from .forms import UserForm, StudentForm, TrainerForm, StaffForm
from .models import Student, Trainer, Staff
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import Admin

def create_student_account(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])
            user.save()
            Student.objects.create(user=user)
            return redirect('success')
    else:
        user_form = UserForm()
    return render(request, 'create_account.html', {'form': user_form, 'account_type': 'Student'})

def create_trainer_account(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])
            user.save()
            Trainer.objects.create(user=user)
            return redirect('success')
    else:
        user_form = UserForm()
    return render(request, 'create_account.html', {'form': user_form, 'account_type': 'Trainer'})

def create_staff_account(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])
            user.save()
            Staff.objects.create(user=user)
            return redirect('success')
    else:
        user_form = UserForm()
    return render(request, 'create_account.html', {'form': user_form, 'account_type': 'Staff'})

def success(request):
    return render(request, 'success.html')

# User login redirect to the respective role :


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Check user role and redirect accordingly
            if hasattr(user, 'student'):
                return redirect('student_dashboard')
            elif hasattr(user, 'trainer'):
                return redirect('trainer_dashboard')
            elif hasattr(user, 'staff'):
                return redirect('staff_dashboard')
            else:
                return render(request, 'login.html', {'error': 'User role not found!'})
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    return render(request, 'login.html')

@login_required
def student_dashboard(request):
    return render(request, 'student_dashboard.html')

@login_required
def trainer_dashboard(request):
    return render(request, 'trainer_dashboard.html')

@login_required
def staff_dashboard(request):
    return render(request, 'staff_dashboard.html')



@login_required
def create_admin(request):
    if not request.user.is_superuser:  # Only SuperAdmin can create Admins
        return render(request, '403.html')  # Forbidden page
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])
            user.is_staff = True  # Mark as staff to allow admin panel access
            user.save()
            Admin.objects.create(user=user)
            return redirect('success')
    else:
        user_form = UserForm()
    return render(request, 'create_admin.html', {'form': user_form})


# @login_required
# def admin_panel(request):
#     if not hasattr(request.user, 'admin'):  # Check if the user is an Admin
#         return render(request, '403.html')  # Forbidden page
#     return render(request, 'admin_dashboard.html')


# =============================================

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Student, Trainer, Staff
from .forms import UserForm, ProfileForm

@login_required
def admin_panel(request):
    # Admin dashboard
    return render(request, 'admin_dashboard.html')

@login_required
def manage_users(request):
    if not hasattr(request.user, 'admin'):
        return render(request, '403.html')  # Forbidden
    students = Student.objects.all()
    trainers = Trainer.objects.all()
    staff = Staff.objects.all()
    return render(request, 'manage_users.html', {
        'students': students,
        'trainers': trainers,
        'staff': staff,
    })

@login_required
def create_user(request, role):
    if not hasattr(request.user, 'admin'):
        return render(request, '403.html')  # Forbidden
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])
            user.save()
            if role == 'student':
                Student.objects.create(user=user, **profile_form.cleaned_data)
            elif role == 'trainer':
                Trainer.objects.create(user=user, **profile_form.cleaned_data)
            elif role == 'staff':
                Staff.objects.create(user=user, **profile_form.cleaned_data)
            return redirect('manage_users')
    else:
        user_form = UserForm()
        profile_form = ProfileForm()
    return render(request, 'create_user.html', {
        'user_form': user_form,
        'profile_form': profile_form,
        'role': role,
    })

@login_required
def update_user(request, user_id):
    if not hasattr(request.user, 'admin'):
        return render(request, '403.html')  # Forbidden
    user = get_object_or_404(User, id=user_id)
    profile = (
        Student.objects.filter(user=user).first() or
        Trainer.objects.filter(user=user).first() or
        Staff.objects.filter(user=user).first()
    )
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=user)
        profile_form = ProfileForm(request.POST, instance=profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('manage_users')
    else:
        user_form = UserForm(instance=user)
        profile_form = ProfileForm(instance=profile)
    return render(request, 'update_user.html', {
        'user_form': user_form,
        'profile_form': profile_form,
    })

@login_required
def delete_user(request, user_id):
    if not hasattr(request.user, 'admin'):
        return render(request, '403.html')  # Forbidden
    user = get_object_or_404(User, id=user_id)
    user.delete()
    return redirect('manage_users')

@login_required
def restrict_user(request, user_id):
    if not hasattr(request.user, 'admin'):
        return render(request, '403.html')  # Forbidden
    user = get_object_or_404(User, id=user_id)
    user.is_active = False  # Disable account
    user.save()
    return redirect('manage_users')
