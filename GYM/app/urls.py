from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('about',views.about,name='about'),
 
    path('schedule',views.schedule,name='schedule'),
    
    
    
    path("adminlogin/", views.adminlogin, name="adminlogin"),
    path("AdminRegistration/", views.AdminRegistration, name="AdminRegistration"),
    
    path("adminDashboard/", views.adminDashboard, name="adminDashboard"),
       
    path("adminloginpage_fetch/", views.adminloginpage_fetch, name="adminloginpage_fetch"),
    path("aregistration/", views.aregistration, name="aregistration"),

    
    
    path('form/',views.form,name='form'),
    
    path('allrecord/',views.allrecord,name='allrecord'),
    
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/',views.delete,name='delete'),
   
]