from django.urls import path
from . import views

urlpatterns = [
    path('', views.quiz_index, name='quiz_index'),
    path("<int:pk>/", views.quiz_detail, name="quiz_detail"),
    path("<category>/", views.quiz_category, name="quiz_category"),
    path('addQuestion/', views.addQuestion, name='addQuestion'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutPage, name='logout'),
    path('register/', views.registerPage, name='register'),
]
