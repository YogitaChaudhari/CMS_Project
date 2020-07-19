
from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('', views.indexpage),
    path('adduserpage', views.adduserpage),
    path('adduser', views.adduser),
    path('userlist', views.userlist),
    path('deleteUser/<str:email>', views.deleteUser),
    path('editUser', views.editUser),
    path('updateUser', views.updateUser),
    path('addcomplaintpage', views.addcomplaintpage),
    path('addcomplaint', views.addcomplaint),
    path('complaintlist', views.complaintlist),
    path('addloginpage',views.addloginpage),
    path('login', views.login),
    path('addsignUpPage', views.addsignUpPage),
    path('signUp', views.signUp),
    path('LogOut', views.LogOut),
    path('deleteComplaint/<int:id>',views.deleteComplaint),
    path('editComplaint',views.editComplaint),
    path('updateComplaint', views.updateComplaint),
    path('homepage', views.homepage),
    path('About', views.About),
    path('Contact', views.Contact),
    path('userComplaint', views.userComplaint),
    path('editProfilepage', views.editProfilepage),
    path('editProfile', views.editProfile),
]








