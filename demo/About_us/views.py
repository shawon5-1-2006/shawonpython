from django.http import HttpResponse
from django.shortcuts import render
from About_us.models import Teachers

# Create your views here.
def about_us(request):
    return render(request, 'about/about.html')

def Teachersinfo(request):
    teach = Teachers.objects.all()
    return render (request, 'about/T.html', {'thr': teach})