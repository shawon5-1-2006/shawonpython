from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def machine_learning(request):

    course = 'machine learning'
    teachers = {'name': ['shawon','shakib','hasan']}


    return render(request, 'machine_learning/masin_learning.html',context= teachers)

def dtml(request):
    return render(request, 'machine_learning/DT.html')

def knnc(request):
    return render(request, 'machine_learning/knn.html')
 
def rendom(request):
    return render(request, 'machine_learning/readome_forest.html')

def boot(request):
    return render(request, 'machine_learning/boot.html')


    