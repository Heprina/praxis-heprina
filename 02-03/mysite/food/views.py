from django.db.models.fields.json import DataContains
from django.shortcuts import redirect, render

from . import models
def index (req):
    return render (req, 'home.html')

# Create your views here.
def index(request):
    if request.POST : 
        models.Makanan.objects.create(
            nama = request.POST['nama'],
            jenis = request.POST['jenis'],
            harga = request.POST['harga']           
        )
        return redirect('/')
    makanan = models.Makanan.objects.all()
    return render (request, 'index.html', {
        'isi' :makanan,
        })

def hapus(request, id):
    models.Makanan.objects.filter(pk=id).delete()
    return redirect('/')

def detail (request, id):
    makanan = models.Makanan.objects.filter(pk=id).first()
    return render (request, 'detail.html', {
        'isi' :makanan
    })

def edit (request, id):
    if request.POST:
        input = request.POST["name"]
        print(input)
        models.Makanan.objects.filter(id=id).update(Makanan = input )
        return redirect('/')

    data = models.Makanan.objects.filter(id=id).first()
    return render (request, "edit.html", {
        "detailData": data,
    })  

