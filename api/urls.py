from django.urls import path

from . import views

urlpatterns = [
    path('', views.upload, name='upload'),
    path('api/',views.api,name='api')
]
