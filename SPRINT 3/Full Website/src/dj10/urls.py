from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home', views.homePage, name="home"),
    path('services', views.services, name="services"),
    path('about', views.about, name="about"),
    path('contact', views.contact, name="contact"),
    path('contact_form/create', views.contact_form),
]

urlpatterns += staticfiles_urlpatterns()