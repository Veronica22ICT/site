from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('', views.home, name='home'),
    path('info/', views.info, name="info"),
    path('types/', views.types, name='types'),
    path('advice/', views.advice, name='advice'),
    path('knives/', views.knives_view, name='knives'),
    path('cares/', views.cares_view, name='cares'),
    path('repairs/', views.repairs_view, name='repairs'),
    path('knife/<int:id>/', views.knife_detail, name='knife_detail'),
    path('repair/<int:id>/', views.repair_detail, name='repair_detail'),
    path('care/<int:id>/', views.care_detail, name='care_detail'),
    path('order/<str:category>/<int:product_id>/', views.make_order, name='make_order'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

