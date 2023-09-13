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


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class DeviceViewSet(viewsets.ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer

class DeviceLogViewSet(viewsets.ModelViewSet):
    queryset = DeviceLog.objects.all()
    serializer_class = DeviceLogSerializer