from django import forms
from django.contrib.auth.models import User
from .models import Student, Trainer, Staff

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = []

class TrainerForm(forms.ModelForm):
    class Meta:
        model = Trainer
        fields = []

class StaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = []
