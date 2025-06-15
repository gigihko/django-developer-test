"""
URL configuration for modular_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, include

# modular_project/urls.py
from module_engine.models import Module
from module_engine.utils import get_active_module_urls
from example_module.models import Product
from django.contrib.auth import views as auth_views
from example_module.forms import BootstrapAuthenticationForm

urlpatterns = [
    path('admin/', admin.site.urls),
    path('module/', include('module_engine.urls')),

    path('', auth_views.LoginView.as_view(authentication_form=BootstrapAuthenticationForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/login/'), name='logout'),
]

urlpatterns += get_active_module_urls()

