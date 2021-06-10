from django.shortcuts import render

from rest_framework import viewsets


from .serializers import StaffSerializer
from .models import Staff


class StaffViewSet(viewsets.ModelViewSet):
    queryset = Staff.objects.all().order_by('surname')
    serializer_class = StaffSerializer

# Create your views here.
