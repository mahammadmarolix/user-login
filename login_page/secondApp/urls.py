from django.urls import path
from . import views

urlpatterns = [
    path("",views.register_page,name='register_page'),
    path("login",views.login_page,name='login'),
    path("home",views.home_page,name='home'),
]