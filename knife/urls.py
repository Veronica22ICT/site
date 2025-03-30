from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('info/', views.info, name="info"),
    path('types/', views.types, name='types'),
    path('links/', views.links, name='links'),
    path('advice/', views.advice, name='advice'),

]

