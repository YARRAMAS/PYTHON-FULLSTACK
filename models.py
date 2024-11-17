from django.db import models

from bson import ObjectId

class Employee(models.Model):
    id = models.CharField(max_length=24, primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email_id = models.EmailField(max_length=100, unique=True)
    mobile_no = models.CharField(max_length=15)
    birth_date = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=6)
    address = models.TextField()
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    skills = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
