from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import      ApplyViewSet
from rest_framework import routers
from rest_framework import permissions





router = routers.DefaultRouter()

router.register('Apply', views.ApplyViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('api/', include(router.urls)),
    path('Apply/', views.Apply, name='Apply'),

   
] 
static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
