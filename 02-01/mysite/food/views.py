from django.shortcuts import redirect, render
from . import models

# Create your views here.
def index (req):
    if req.POST:
        models.Makan.objects.create(nama= req.POST['nama'])
        return redirect('/')

    makan = models.Makan.objects.all()
    return render (req, 'index.html', {
        'isimakan': makan,
    })





    