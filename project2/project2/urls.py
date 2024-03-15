"""
URL configuration for project2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

from firstapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/', views.show),
    path('rcv/', views.receive,name="rcv"),
    path('test/lgn/', views.dologin),
    path('test/sgn/', views.dosignup),
    path('test/lgn/sgn/', views.dosignup),
    path('test/sgn/lgn/', views.dologin),
    path('test/dog/', views.extra),
    path('test/cat/', views.mycat),
    path('test/inf',views.myinfo),
    path('test/meal/', views.mymeal),
    path('test/health/', views.myhealth),
    path('test/act/', views.myact),
    path('test/feed/', views.showfeedback),
    path('fdbk/', views.dofeedback,name="fdbk"),
    path('tksig/', views.takesignup,name="tksig"),
    path('test/ord/',views.myorder),
    path('log/',views.takelogin,name="log"),
    path('ordt/',views.getorder,name="ordt"),
    path('rpt/',views.conreport),
    path('rpt1/',views.logreport),
]

