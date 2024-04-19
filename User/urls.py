from django.urls import path, include
from rest_framework import routers

from User import views

router = routers.SimpleRouter()
router.register(r'user', views.UserViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls))
]