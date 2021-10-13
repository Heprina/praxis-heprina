from django.db import models
from django.db.models.base import Model

# Create your models here.
class Makanan(models.Model):
    jenis = models.CharField(default = '',max_length=30)
    nama = models.TextField(default= '', max_length=30)
    harga = models.IntegerField()

