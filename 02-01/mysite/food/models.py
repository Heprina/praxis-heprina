from django.db import models

# Create your models here.
class Makanan(models.Model):
    jenis = models.CharField(max_length=200)
    nama = models.TextField()
    harga = models.IntegerField()


class Minuman(models.Model):
    jenis = models.CharField(max_length=200)
    nama = models.TextField()
    harga = models.IntegerField()


class pesanan(models.Model):
    nama_makanan = models.CharField(max_length=200)
    jumlah_pesanan_makanan = models.CharField(max_length=200)
    nama_minuman = models.IntegerField()
    jumlah_pesanan_makanan = models.CharField(max_length=200)



