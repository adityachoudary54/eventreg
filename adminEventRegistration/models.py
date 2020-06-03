from django.db import models

# Create your models here.
class Announcements(models.Model):
    date=models.DateField(auto_now_add=True)
    info=models.CharField(max_length=1000) 
    location=models.CharField(max_length=100) 