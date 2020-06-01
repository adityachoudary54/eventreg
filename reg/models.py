from django.db import models

# Create your models here.
class Register(models.Model):
    regId=models.CharField(default='',max_length=40)
    date=models.DateField(auto_now_add=True)
    username=models.CharField(max_length=200)
    mobile=models.CharField(max_length=20)
    email=models.EmailField()
    idcard=models.FileField(upload_to='registerImages/')
    regType=models.CharField(max_length=20)
    noTickets=models.CharField(max_length=10)