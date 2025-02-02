"""
URL configuration for miniblog project.

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
from blog import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('deshboard/',views.deshboard,name='deshboard'),
    path('user_logout/',views.user_logout,name='user_logout'),
    path('signup/',views.signup,name='signup'),
    path('login/',views.user_login,name='login'),
    path('addpost/',views.addpost,name='addpost'),
    path('update/<int:id>',views.updatepost,name='updatepost'),
    path('delete/<int:id>',views.deletepost,name='deletepost'),
]
