from rest_framework import viewsets, permissions
from django_filters import rest_framework as filters
from rest_framework.authentication import BasicAuthentication, TokenAuthentication, SessionAuthentication

from .serializers import StaffSerializer
from .models import Staff


class StaffViewSet(viewsets.ModelViewSet):

    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [BasicAuthentication, TokenAuthentication, SessionAuthentication]
    queryset = Staff.objects.all().order_by('surname')
    serializer_class = StaffSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('level',)
    http_method_names = ["get",]
