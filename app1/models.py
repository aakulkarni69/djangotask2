from django.db import models

class student(models.Model):
    f_name = models.CharField(max_length=20)
    l_name = models.CharField(max_length=20)
    ph_no = models.CharField(max_length=15)
    email = models.CharField(max_length=30)
    gender = models.CharField(max_length=10)
