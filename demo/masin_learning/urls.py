from django.urls import path
from . import views

urlpatterns = [
    path('machin/',views.machine_learning, name='ml'),
    path('deml/',views.dtml, name='dt'),
    path('knc/',views.knnc),
    path('ren/',views.rendom),
    path('bot/',views.boot, name='bt'),
]