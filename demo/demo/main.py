from django.http import HttpResponse

def first(request):
    return HttpResponse('<h1>Hello</h1>')