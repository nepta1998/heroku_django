from django.urls import path, include
from rest_framework import routers
from .views import MessageViewSet

ROUTER = routers.DefaultRouter()
ROUTER.register("messages", MessageViewSet)
urlpatterns = [
    # http://localhost:8000/v1.0/api/<router-viewsets>
    path('/', include(ROUTER.urls)),
]
