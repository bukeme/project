from django.db import models
from django.conf import settings
from django.utils import timezone

User = settings.AUTH_USER_MODEL

# Create your models here.

class Project(models.Model):
	title = models.CharField(max_length=200)
	case_study = models.CharField(max_length=200)

	def __str__(self):
		return self.title

	@property
	def allocated(self):
		if self.student_set.all().count() > 0:
			return True
		return False

	@property
	def group_project(self):
		if self.student_set.all().count() > 1:
			return True
		return False

class Student(models.Model):
	DEPARTMENTS = (
		('Agricultural Engineering', 'Agricultural Engineering'),
		('Electrical Engineering', 'Electrical Engineering'),
		('Computer Engineering', 'Computer Engineering'),
		('Chemical Engineering', 'Chemical Engineering'),
		('Petroleum Engineering', 'Petroleum Engineering'),
		('Mechanical Engineering', 'Mechanical Engineering'),
		('Food Engineering', 'Food Engineering'),
		('Civil Engineering', 'Civil Engineering'),
	)

	LEVEL = (
		('500 Level', '500 Level'),
		('Spill Over', 'Spill Over'),
	)

	user = models.OneToOneField(User, on_delete=models.CASCADE)
	reg_no = models.CharField(max_length=50)
	department = models.CharField(max_length=100, choices=DEPARTMENTS)
	level = models.CharField(max_length=50, choices=LEVEL, default='500 Level')
	project = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True, blank=True)
	date_joined = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return f'{self.user.first_name} {self.user.last_name}'
