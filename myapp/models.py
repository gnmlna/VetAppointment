from django.db import models
from datetime import datetime   

class Patient(models.Model):
    name=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    email=models.EmailField(max_length=254)
    date = models.DateField()
    time=models.TimeField() 
    address=models.CharField(max_length=100)