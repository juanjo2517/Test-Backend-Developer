# Django
from django.urls import include, path

# Django REST Framework
from rest_framework.routers import DefaultRouter

# Vies
from .views import fifa_api as view_fifa_api

router = DefaultRouter()

router.register(r'v1', view_fifa_api.PlayerViewSet, basename="player")

urlpatterns = [
    path('', include(router.urls))
]


