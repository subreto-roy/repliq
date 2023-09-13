from rest_framework import serializers
from .models import Company, Employee, Device, DeviceLog

# Serializer for the Company model
class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

