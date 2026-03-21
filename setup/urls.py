from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
import desafioBackend.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('desafioBackend.urls')),
]
