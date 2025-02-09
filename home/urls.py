from django.contrib import admin
from django.urls import path, include
from home import views


urlpatterns = [ 
    path('',views.index, name="home"),
    path('home',views.index, name="home"),
    path('login',views.login, name="login"),
    path('signup/',views.signup, name="signup"),
    path('logout',views.logoutUser, name="logout"),
    path('Healthcare',views.Healthpage, name="healthcare"),
    path('science',views.sciencePage, name="science"),
    path('computer',views.computerPage, name="computer"),
    path('Generateimage',views.ImgGenerator, name="Generateimage"),
]
