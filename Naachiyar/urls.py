"""construction URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from Naachiyar import views
app_name='Naachiyar'

urlpatterns = [

    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('', views.home, name='home'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('contact/',views.contact,name='contact'),
    path('projects/',views.projects,name='projects'),
    path('alogin/',views.alogin,name='alogin'),
    path('quote/',views.quote,name='quote'),
    path('job/',views.job,name='job'),
    path('feedback/',views.feedback,name='feedback'),
    path('worker/',views.worker_list,name='worker_list'),
    path('addworker/',views.add_worker,name='add_worke'),
    path('update_worker/<int:id>/',views.update_worker,name='update_worker'),
    path('delete_worker/<int:id>/', views.delete_worker, name='delete_worker'),
    path('project/',views.project_list,name='project_list'),
    path('addproject/',views.add_project,name='add_project'),
    path('delete_project/<int:id>/', views.delete_project, name='delete_project'),
    path('update_project/<int:id>/',views.update_project,name='update_project'),
    path('adminfeedback/',views.Feedback_show,name='adminfeedback'),
    path('adminquote/',views.Quote_show,name='adminquote'),
    path('hiering/',views.hiering,name='hiering'),
    path('delete_hiering/<int:id>/', views.delete_hiering, name='delete_hiering'),  
]