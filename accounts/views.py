from django.shortcuts import render, redirect
from .forms import UserForm, StudentForm, TrainerForm, StaffForm
from .models import Student, Trainer, Staff

def create_student_account(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user.password)
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
            user.set_password(user.password)
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
            user.set_password(user.password)
            user.save()
            Staff.objects.create(user=user)
            return redirect('success')
    else:
        user_form = UserForm()
    return render(request, 'create_account.html', {'form': user_form, 'account_type': 'Staff'})
