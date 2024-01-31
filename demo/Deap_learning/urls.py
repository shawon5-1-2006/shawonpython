from django.urls import path
from . import views

urlpatterns = [
    path('d/',views.deap_learning, name='deap'),
    path('registor/', views.registation)
]
