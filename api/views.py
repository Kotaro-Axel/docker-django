from .models import Owner
from .serializers import OwnerSerializer

from rest_framework import viewsets, views, filters, generics
from django.shortcuts import render
# Create your views here.

class OwnerViewSet(viewsets.ModelViewSet):
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer
    