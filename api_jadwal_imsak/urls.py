from django.contrib import admin
from django.urls import path, include
from api_jadwal_imsak.views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register('jadwal', jadwal_imsakViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
