"""docpait URL Configuration

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
from django.contrib import admin
from django.urls import path,include
from taskapp import views
from django.contrib.auth.views import LoginView,LogoutView


app_name = "taskapp"
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home_view,name=''),
    path('',include('blog.urls')),


    # path('aboutus', views.aboutus_view),
    # path('contactus', views.contactus_view),

    path('doctorclick/', views.doctorclick_view),
    path('patientclick/', views.patientclick_view),

    # # # path('adminsignup', views.admin_signup_view),
    path('doctorsignup', views.doctor_signup_view,name='doctorsignup'),
    path('patientsignup', views.patient_signup_view),
    
    # # # path('adminlogin', LoginView.as_view(template_name='taskapp/adminlogin.html')),
    path('doctorlogin', LoginView.as_view(template_name='taskapp/doctorlogin.html')),
    path('patientlogin', LoginView.as_view(template_name='taskapp/patientlogin.html')),


    path('afterlogin', views.afterlogin_view,name='afterlogin'),
    path('logout', LogoutView.as_view(template_name='taskapp/index.html'),name='logout'),


    path('doctor-dashboard', views.doctor_dashboard_view,name='doctor-dashboard'),
    path('patient-dashboard', views.patient_dashboard_view,name='patient-dashboard'),
]
