from django.db import models

# Create your models here.


class Register(models.Model):
    Username=models.CharField(max_length=30,default="string")
    email=models.CharField(max_length=50)
    phone=models.CharField(max_length=20,default='0000')
    password=models.CharField(max_length=30,default="pass")
    def __str_(self):
        return self.Username
