from django.urls import path

from. import views

urlpatterns =  [
    path('', views.index),
    path('foods/',views.input_makanan),
    path('drink/',views.input_minuman),
    path('update/<id>/',views.menu_utama),
    path('hapus/<id>/',views.hapus),
]