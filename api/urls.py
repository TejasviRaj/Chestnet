from django.urls import path

from . import views

urlpatterns = [
    path('', views.upload, name='upload'),
    path('api/',views.api,name='api'),
    path('yash/', views.first, name='first'),
    path('second/', views.second, name='second'),
    path('mult/', views.mult, name='mult')

]
