from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def deap_learning(request):
    return render(request, 'deap_learning/deap_learning.html')

def registation(request):
    if request.method == "POST":
        fm = UserCreationForm(request.POST)
        if fm.is_valid():
            fm.save()
    else:
     fm = UserCreationForm
    return render(request, 'deap_learning/register.html', {'form': fm} )