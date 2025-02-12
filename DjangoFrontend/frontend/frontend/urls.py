"""
URL configuration for frontend project.

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
import handleRequests.userRequests
from handleRequests.userRequests.forms.signUpView import signUp_view
import handleRequests
import DjangoFrontend.frontend.frontend.home.homeView  
urlpatterns = [
    path('admin/', admin.site.urls),
    path('signUp/', signUp_view,name='signUp_view'),
    path('',DjangoFrontend.frontend.frontend.home.homeView.form_view),
    #path('login/')

]
