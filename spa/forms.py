from django import forms
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from allauth.account.forms import SignupForm
from .models import Student, Project

# User = settings.AUTH_USER_MODEL

class UserRegistrationForm(SignupForm):
	first_name = forms.CharField(max_length=200)
	last_name = forms.CharField(max_length=200)
	# email = forms.EmailField()
	class Meta:
		model = User 
		fields = ['first_name', 'last_name', 'email']
		# fields = '__all__'

class StudentForm(forms.ModelForm):
	class Meta:
		model = Student 
		fields = ['reg_no', 'department', 'level']

class LoginForm(forms.Form):
	email = forms.EmailField()
	password = forms.CharField(widget=forms.PasswordInput)

class UserForm(forms.ModelForm):
	class Meta:
		model = User 
		fields = ['first_name', 'last_name', 'email']

class ProjectForm(forms.ModelForm):
	class Meta:
		model = Project 
		fields = ['title', 'case_study']

# class UserRegisterForm(UserRegistrationForm):
# 	class Meta:
# 		model = User 
# 		fields = ['']
