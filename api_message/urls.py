from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .views import MessageViewSet

router = routers.DefaultRouter()
router.register("messages", MessageViewSet)
urlpatterns = [
    # http://localhost:8000/v1.0/api/<router-viewsets>
    path('/', include(router.urls)),
]
