from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE

# Create your models here.
class makanan(models.Model):
    jenis = models.CharField(default = '',max_length=30)
    nama = models.TextField(default= '', max_length=30)
    harga = models.IntegerField()

class minuman(models.Model):
    jenis = models.CharField(default = '',max_length=30)
    nama = models.TextField(default= '', max_length=30)
    harga = models.IntegerField()

class home (models.Model):
    data_makanan = models.ForeignKey(makanan, on_delete=CASCADE)
    data_minuman = models.ForeignKey(minuman, on_delete=CASCADE)