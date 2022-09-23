from django.urls import path
from . import views

urlpatterns = [
    path('', views.log_in, name='log_in'),
    path('login', views.account_login, name="login"),
    path('register', views.create_account, name="register"),
    path("home",views.home, name="home")
]