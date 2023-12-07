from django.urls import path
from . import views


urlpatterns = [
    path('', views.studentView, name=''),
    path('register/', views.StudentRegister, name='register'),
    path('update/<int:id>/', views.StudentUpdate, name='update'),
    path('delete/<int:id>/', views.StudentDelete, name='delete'),
]
