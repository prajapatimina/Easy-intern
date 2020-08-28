from django.urls import path

from .import views
app = 'students'

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.sregister, name='student_register'),
    path('login/',views.slogin, name ='student_login'),
    
]