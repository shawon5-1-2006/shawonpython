from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def python(request):
    return render(request, 'deap_learning/deap_learning.html')
