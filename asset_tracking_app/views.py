from django.shortcuts import render, get_object_or_404, redirect
from .models import Company, Employee, Device

# Import the necessary modules from Django REST Framework
from rest_framework import viewsets
from .models import Company, Employee, Device, DeviceLog
from .serializers import CompanySerializer, EmployeeSerializer, DeviceSerializer, DeviceLogSerializer

# ViewSets for API views
class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


