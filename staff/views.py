from rest_framework import viewsets, permissions
from django_filters import rest_framework as filters

from .serializers import StaffSerializer
from .models import Staff


class StaffViewSet(viewsets.ModelViewSet):

    permission_classes = [permissions.IsAuthenticated]
    queryset = Staff.objects.all().order_by('surname')
    serializer_class = StaffSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('level',)
    http_method_names = ["get",]
