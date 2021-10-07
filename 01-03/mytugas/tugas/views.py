from django.db.models.fields.json import DataContains
from django.shortcuts import  render

from . import models
#create your views here.


def index(request):
    if request.POST : 
        # data = request.POST ['name']
        # print (data)
        #input data ke database
        models.tugas.objects.create(name = request.POST ['name'])
        #nampilin datanya
    data2 = models.tugas.objects.all()

    return render (request, 'index.html', {'isi' :data2})
   
