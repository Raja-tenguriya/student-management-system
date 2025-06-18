from django.db import models

class student(models.Model):
    roll = models.IntegerField()
    name = models.CharField(max_length=60)
    cls = models.CharField(max_length=60, default=' ')
    city = models.CharField(max_length=100)
