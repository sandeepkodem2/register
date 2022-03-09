from django.urls import path
from register import views

app_name='register'
urlpatterns=[
    path('home',views.home,name='home'),
    path('success',views.success,name='success')


]