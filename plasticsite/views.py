from django.shortcuts import render
from django.template import loader
# Create your views here.

def info(request):
    return render(request, 'plasticsite/info.html')
def advantages(request):
    return render(request, 'plasticsite/advantages.html')
def you(request):
    return render(request, 'plasticsite/you.html')

 
