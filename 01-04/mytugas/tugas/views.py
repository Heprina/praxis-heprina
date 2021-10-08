from django.db.models.fields.json import DataContains
from django.shortcuts import  redirect, render

from . import models
#create your views here.


def index(request):
    if request.POST : 
        data = request.POST ['name']
        print (data)
        #input data ke database
        models.tugas.objects.create(name = data)
        #nampilin datanya
    data2 = models.tugas.objects.all()
    print(data2)

    return render (request, 'index.html', {'isi' :data2})
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
        input = request.POST["name"]
        print(input)
        models.tugas.objects.filter(id = id).update(name = input)
        return redirect('/')

    data = models.tugas.objects.filter(id = id).first()
    return render (request, "edit.html", {
        "detailData": data,
    })  