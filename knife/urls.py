from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('', views.home, name='home'),
    path('info/', views.info, name="info"),
    path('types/', views.types, name='types'),
    path('types/', views.knife_list, name='knife_list'),
    path('advice/', views.advice, name='advice'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

