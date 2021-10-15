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
        return redirect('/foods')
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
        return redirect('/drink')
    minuman = models.minuman.objects.all()
    return render (req, 'index.minuman/index.html', {
        'data_minuman' :minuman,
        })

def hapusmakanan(request, id):
    models.makanan.objects.filter(pk=id).delete()
    return redirect('/foods')

def hapusminuman(request, id):
    models.minuman.objects.filter(pk=id).delete()
    return redirect('/drink')

def menu_utama (req, id):
    menu = models.makanan.objects.filter(pk=id).first()
    return render (request, 'home.html', {
        'menu' :menu
    })

def editmakanan(request, id):
    if request.POST:
        models.makanan.objects.filter(id=id).update(
            nama = request.POST['nama'],
            jenis = request.POST['jenis'],
            harga = request.POST['harga']           
        )
        return redirect('/foods')

    data = models.makanan.objects.filter(id=id).first()
    return render (request, "index.makanan/index.html", {
        "data_makanan":editmakanan,
    })


def editminuman(request, id):
    if request.POST:
        models.minuman.objects.filter(id=id).update(
            nama = request.POST['nama'],
            jenis = request.POST['jenis'],
            harga = request.POST['harga']           
        )
        return redirect('/drink')

    data = models.minuman.objects.filter(id=id).first()
    return render (request, "index.minuman/index.html", {
        "data_minuman":editminuman,
    })
