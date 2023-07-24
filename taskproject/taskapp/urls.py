from . import views
from django.urls import path

urlpatterns = [

    path('',views.demo,name='home'),

    # path('login',views.login,name='login')

    ]