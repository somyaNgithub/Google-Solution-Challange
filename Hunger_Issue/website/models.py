from django.db import models


class MyModel(models.Model):
    uid = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    number = models.IntegerField()
