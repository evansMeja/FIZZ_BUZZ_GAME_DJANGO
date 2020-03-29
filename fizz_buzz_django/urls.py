"""fizz_buzz_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from fizz_buzz_app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index,name="index"),
    path('play', play,name="play"),
    path('login', Login,name="login"),
    path('register', register,name="register"),
    path('rules', rules,name="rules"),
    path('bestplayers', bestplayers,name="bestplayers"),
    path('validateregister', validateregister,name="validateregister"),
    path('savenewscore', savenewscore,name="savenewscore"),
    path('resetscores', resetscores,name="resetscores"),
    path('validatemylogin', validatemylogin,name="validatemylogin"),
    path('Logout', Logout,name="Logout"),
]
