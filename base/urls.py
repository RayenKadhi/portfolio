from django.urls import path
from . import views



urlpatterns=[
    path('', views.homePage, name='home'),
    path('project/<str:pk>/', views.projectPage, name='project'),
    path('add-project/', views.addProject, name='add-project'),
    path('edit-project/<str:pk>/', views.editProject, name='edit-project'),
    path('inbox/', views.inboxPage, name='inbox'),
    path('message/<str:pk>/', views.messagePage, name='message'),
    path('add-skill/', views.addSkill, name='add-skill'),
    path('add-endorsement/', views.addEndorsement, name='add-endorsement'),
    path('project1/<str:pk>/', views.projectPage1, name='project1'),
    path('edit-project1/<str:pk>/', views.editProject1, name='edit-project1'),
    path('contactMe1/', views.contactMe, name='contactMe1'),





]