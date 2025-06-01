"""
URL configuration for OverDriveFXBackend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from main.views.home.home import home
from main.views.testimonial.testimonial_list import testimonial_list
from main.views.testimonial.testimonial_create import testimonial_create
from main.views.testimonial.testimonial_admin import testimonial_admin
from main.views.testimonial.testimonial_delete import testimonial_delete
from main.views.testimonial.testimonial_edit import testimonial_edit


app_name = "main"
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('testimonial/', testimonial_list, name='testimonial'),
    path('testimonial/create', testimonial_create, name='testimonial-create'),
    path('testimonial/admin', testimonial_admin, name='testimonial-admin'),
    path("<str:pk>/delete/", testimonial_delete, name="testimonial-delete"),
      path("<str:pk>/edit/", testimonial_edit,   name="testimonial-edit")
]
