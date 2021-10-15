from django.urls import path

from. import views

urlpatterns =  [
    path('',views.index),
    path('foods/',views.input_makanan),
    path('drink/',views.input_minuman),
    path('update/<id>/',views.menu_utama),
    path('foods/hapus/<id>',views.hapusmakanan),
    path('drink/hapus/<id>',views.hapusminuman),
    path('foods/edit/<id>',views.editmakanan),
    path('drink/edit/<id>',views.editminuman),
]