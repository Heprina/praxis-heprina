from django.http import request
from django.shortcuts import redirect, render

from . import models

# Create your views here.
def index (req):
    menu_utama =models.home.objects.all()
    return render (req, 'index.home/home.html', {
        'data': menu_utama,
    })

def input_makanan(req):
    if req.POST : 
        models.makanan.objects.create(
            nama = req.POST['nama'],
            jenis = req.POST['jenis'],
            harga = req.POST['harga']           
        )
        return redirect('foods/')
    makanan = models.makanan.objects.all()
    return render (req, 'index.makanan/index.html', {
        'data_makanan' :makanan,
        })
    

def input_minuman(req):
    if req.POST : 
        models.minuman.objects.create(
            nama = req.POST['nama'],
            jenis = req.POST['jenis'],
            harga = req.POST['harga']           
        )
        return redirect('minum/')
    minuman = models.makanan.objects.all()
    return render (req, 'index.minuman/index.html', {
        'data_minuman' :minuman,
        })

def hapus(request, id):
    models.makanan.objects.filter(pk=id).delete()
    return redirect('foods/')

def menu_utama (req, id):
    menu = models.makanan.objects.filter(pk=id).first()
    return render (request, 'detail.html', {
        'menu' :menu
    })

