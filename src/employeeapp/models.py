from django.db import models

class EmployeeData(models.Model):
    first_name=models.CharField(max_length=40)
    last_name=models.CharField(max_length=40)
    email=models.EmailField(max_length=40)
    salary=models.IntegerField()
    job=models.CharField(max_length=40)
    company=models.CharField(max_length=40)
    location=models.CharField(max_length=40)
