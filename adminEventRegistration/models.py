from django.db import models

# Create your models here.
class Announcements(models.Model):
    date=models.DateField()
    info=models.CharField(max_length=1000) 
    location=models.CharField(max_length=100) 
    req=models.CharField(max_length=200,default=None) 