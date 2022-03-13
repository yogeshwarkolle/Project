from django.db import models



class Credentials(models.Model):
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=30)
    scode = models.CharField(max_length=10)

class Data(models.Model):
    name = models.CharField(max_length=50)
    phn = models.BigIntegerField(max_length=10)
    email = models.EmailField(max_length=100)

