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



from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import UserForm, StudentForm, TrainerForm, StaffForm
from .models import Student, Trainer, Staff
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

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
