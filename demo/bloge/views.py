from django.http import HttpResponse
from django.shortcuts import render
from . forms import TecharsRegistraton

# Create your views here.
def bloge1(request):
    return render(request, 'bloge/bloge.html')


def showformsdata(request):
    if request.method == 'POST':
        fm = TecharsRegistraton(request.POST)
        if fm.is_valid():
         print(fm)
         print(fm.cleaned_data['passeord'])
         print(fm.cleaned_data['repasseord'])
    else:
     fm = TecharsRegistraton()
     print('This is GET statement')
    return render(request, 'bloge/forms.html', {'form': fm})
    