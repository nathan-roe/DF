"""df URL Configuration"""
from django.contrib import admin
from django.urls import path, include

admin.site.site_header = f'DF Admin Panel - Django'
admin.site.site_title = f'DF Admin'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('communication/', include('communication.urls')),
    path('donation/', include('donation.urls')),
    path('metrics/', include('metrics.urls')),
    path('users/', include('users.urls')),
]
