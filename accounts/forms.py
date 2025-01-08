# from django import forms
# from django.contrib.auth.models import User
# from .models import Student, Trainer, Staff

# class UserForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password']

# class StudentForm(forms.ModelForm):
#     class Meta:
#         model = Student
#         fields = []

# class TrainerForm(forms.ModelForm):
#     class Meta:
#         model = Trainer
#         fields = []

# class StaffForm(forms.ModelForm):
#     class Meta:
#         model = Staff
#         fields = []



# from django import forms
# from django.contrib.auth.models import User
# from .models import Student, Trainer, Staff

# class UserForm(forms.ModelForm):
#     password = forms.CharField(widget=forms.PasswordInput())
#     re_password = forms.CharField(widget=forms.PasswordInput(), label="Re-enter Password")
#     phone_number = forms.CharField(max_length=15)
#     address = forms.CharField(widget=forms.Textarea)
#     dob = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password']

#     def clean(self):
#         cleaned_data = super().clean()
#         password = cleaned_data.get('password')
#         re_password = cleaned_data.get('re_password')

#         if password != re_password:
#             raise forms.ValidationError("Passwords do not match")
#         return cleaned_data

# class StudentForm(forms.ModelForm):
#     class Meta:
#         model = Student
#         fields = []

# class TrainerForm(forms.ModelForm):
#     class Meta:
#         model = Trainer
#         fields = []

# class StaffForm(forms.ModelForm):
#     class Meta:
#         model = Staff
#         fields = []

# class ProfileForm(forms.ModelForm):
#     class Meta:
#         model = Student  # Can be used for Trainer or Staff dynamically
#         fields = []


from django import forms
from django.contrib.auth.models import User
from .models import Student, Trainer, Staff

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'first_name', 'last_name']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Student  # Can be used for Trainer or Staff dynamically
        fields = ['phno', 'address', 'dob']
