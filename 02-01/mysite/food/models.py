from django.db import models

# Create your models here.
class Makan(models.Model):
    nama = models.CharField(default='',max_length=20)
