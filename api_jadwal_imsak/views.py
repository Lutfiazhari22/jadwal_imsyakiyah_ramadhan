from django.shortcuts import render
from .models import jadwal_imsak
from .serializers import jadwal_imsakSerializer
from rest_framework import viewsets

# memanggil database dari mysql

class jadwal_imsakViewSet(viewsets.ModelViewSet):
    queryset = jadwal_imsak.objects.all()
    serializer_class = jadwal_imsakSerializer