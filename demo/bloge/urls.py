from django.urls import path
from . import views

urlpatterns = [
    path('b/',views.bloge1, name='bloge'),
    path('f/', views.showformsdata),
]
