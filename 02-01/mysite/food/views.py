from django.core.checks import messages
from django.http import request
from django.http.response import Http404
from django.shortcuts import redirect, render
from . import models

# Create your views here.
def index(request):
    if request.POST : 
        # print (data)
        #input data ke database
        models.Makanan.objects.create(
            nama = request.POST['nama'],
            jenis = request.POST['jenis'],
            harga = request.POST['harga']
        )
        return redirect('/')
        #nampilin datanya
    data2 = models.Makanan.objects.all()
    # print(data2)
    return render (request, 'index.html', {
        'isi' :data2
        })

def hapus (request, id):
    models.tugas.objects.filter(id = id).delete()
    return redirect('/')


def detail (request, id):
    data = models.tugas.objects.filter(id = id).first()
    print(data)
    return render (request, "detail.html", {
        "detail.data": data
    })  

def edit (request, id):
    if request.POST:
        input = request.POST["makanan"]
        print(input)
        models.tugas.objects.filter(id = id).update(makanan = input)
        return redirect('/')

    data = models.tugas.objects.filter(id = id).first()
    return render (request, "edit.html", {
        "detailData": data,
    })  




    