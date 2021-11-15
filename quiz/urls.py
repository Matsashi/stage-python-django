from django.urls import path
from . import views

urlpatterns = [
    path('', views.quiz, name='quiz'),
    path('addQuestion/', views.addQuestion, name='addQuestion'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutPage, name='logout'),
    path('register/', views.registerPage, name='register'),
]
