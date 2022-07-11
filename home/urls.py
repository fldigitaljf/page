
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('gravar/', views.gravar, name='gravar'),
    path('inscrever/', views.inscrever, name='inscrever'),
    ] 
