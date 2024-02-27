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
    path('contact/',views.contact,name='contact'),
    path('quote/',views.quote,name='quote'),
    path('job/',views.job,name='job'),
    path('feedback/',views.feedback,name='feedback'),
    path('nambi/',views.admin,name='admin'),
<<<<<<< HEAD
    path('worker/',views.worker,name='worker'),
    path('demo/',views.demo,name='demo'),
=======
    path('worker/',views.show_workers,name='show_workers'),
    path('add_worker/',views.add_worker,name='add_worker')
>>>>>>> 8b354f6c965bbefaee23553e9d30edaad2611000
]