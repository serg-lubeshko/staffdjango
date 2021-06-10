from django.shortcuts import render

from rest_framework import viewsets

from .serializers import StaffSerializer
from .models import Staff

class HeroViewSet(viewsets.ModelViewSet):
    queryset = Staff.objects.all().order_by('name')
    serializer_class = StaffSerializer

# Create your views here.
