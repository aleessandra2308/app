from re import template
from django.urls import path
from django.contrib.auth import views as auth_views

from company.views import Home
from .views import *
urlpatterns = [

    path('', Home.as_view(), name='home'),
    path('login/',auth_views.LoginView.as_view(template_name='company/login.html'),
        name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='company/login.html'),
        name='logout'),

    path('idiomas/',IdiomaList.as_view(),name="idiomas"),
    path('frases/',FraseList.as_view(),name="frases"),

]