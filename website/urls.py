"""database2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
# from django.conf import settings
from atexit import register
from django.contrib import admin
from django.urls import path , include
from . import views
from django.conf import settings
from django.conf.urls.static import static 


urlpatterns = [
   
    path("", views.home, name='home'),
    # path("register.html", views.register, name='register'),
    path('login.html',views.loginuser,name="login"),
    path('Contactus.html',views.Contactus,name="Contactus"),
    path('logout.html',views.logoutuser,name="logout"),
    path('__debug__/', include('debug_toolbar.urls')),
    path('who.html',views.whoAreWe,name="who"),
    path('weDo.html',views.WeDo,name="WeDo"),
    path('sustainability.html',views.sustainability,name="sustainability"),
    path('investor.html',views.investor,name="investor"),
    path('career.html',views.career,name="career"),
    path('register.html',views.SaveProfile,name="resume")


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
#    import debug_toolbar
#    urlpatterns += path('__debug__/', include('debug_toolbar.urls'))
