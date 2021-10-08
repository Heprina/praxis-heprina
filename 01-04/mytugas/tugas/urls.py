from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('hapus/<id>/',views.hapus),
    path('detail/<id>/', views.detail),
    path('edit/<id>/', views.edit),
    
]
