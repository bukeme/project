from django.urls import path, include
import allauth.account
from . import views

urlpatterns = [
	path('accounts/signup/', views.student_registration, name='account_signup'),
	path('accounts/login/', views.login, name='account_login'),
	# path('accounts/login/', allauth.account.views.LoginView.as_view(), name='account_login'),
	path('accounts/', include('allauth.account.urls')),
	path('', views.redirect_to_dashboard, name='redirect_to_dashboard'),
	path('<int:pk>/', views.student_dashboard, name='student_dashboard'),
	path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
	path('register-project/', views.register_project, name='register_project'),
	path('project/<int:pk>/', views.project_detail, name='project_detail'),
	path('project-update/<int:pk>/', views.project_update, name='project_update'),
	path('project-delete/<int:pk>/', views.project_delete, name='project_delete'),
	path('project-list/', views.project_list, name='project_list'),
	path('student-list/', views.student_list, name='student_list'),
	path('student-update/<int:pk>/', views.student_update, name='student_update')
]