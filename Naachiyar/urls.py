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
    path('temple/',views.temple,name='temple'),
    path('church/',views.church,name='church'),
    path('mosque/',views.mosque,name='mosque'),
    path('school/',views.school,name='school'),
    path('office/',views.office,name='office'),
    path('factory/',views.factory,name='factory'),
    path('hospital/',views.hospital,name='hospital'),
    path('mall/',views.mall,name='mall'),
    path('alogin/',views.alogin,name='alogin'),
    path('quote/',views.quote,name='quote'),
    path('job/',views.job,name='job'),
    path('feedback/',views.feedback,name='feedback'),
    path('worker/',views.show_workers,name='show_workers'),
    path('project/',views.project_list,name='project_list'),
    path('delete_project/<int:id>/', views.delete_project, name='delete_project'),
    path('add_worker/',views.add_worker,name='add_worker'),
    
    path('adminfeedback/',views.Feedback_show,name='adminfeedback'),
    path('adminquote/',views.Quote_show,name='adminquote'),
    path('hiering/',views.hiering,name='hiering'),
    path('footer/',views.footer,name='footer'),  
]