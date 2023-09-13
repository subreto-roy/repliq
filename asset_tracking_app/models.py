from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=100)
   

class Employee(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
  

class Device(models.Model):
    name = models.CharField(max_length=100)
   

class DeviceLog(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    check_out_date = models.DateTimeField()
    check_in_date = models.DateTimeField()
    condition_when_checked_out = models.CharField(max_length=100)
    condition_when_checked_in = models.CharField(max_length=100)
