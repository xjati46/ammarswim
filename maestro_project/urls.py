"""maestro_project URL Configuration

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
from django.urls import path, include
from main_app.views import (
                            IndexView,
                            RegistrationView,
                            TestTemplateView,
                            DeniedAccessView,
                            CoachProfileCreateView,
                            StudentProfileCreateView,
                            search
                            )
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='main/')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('adm/', include('admin_app.urls')),
    path('coach/', include('coach_app.urls')),
    path('student/', include('student_app.urls')),
    path('main/', IndexView.as_view(), name='index'),
    path(
        'accounts/registration/',
        RegistrationView.as_view(),
        name='registration'),
    path('403/', DeniedAccessView.as_view(), name='denied-access'),
    path('test/', TestTemplateView.as_view(), name='test'),
    path('coach_new/', CoachProfileCreateView.as_view(), name='coach-create'),
    path(
        'student_new/',
        StudentProfileCreateView.as_view(),
        name='student-create'),
    path('search/', search, name='search'),
]
