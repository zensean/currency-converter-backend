# core/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CurrencyRateViewSet

router = DefaultRouter()
router.register(r'rates', CurrencyRateViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api/auth/', include('dj_rest_auth.urls')),
    path('api/auth/register/', include('dj_rest_auth.registration.urls')),
]
