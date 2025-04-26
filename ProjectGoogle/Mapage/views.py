from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def Main(request):
    return render(request, 'Main.html')
def gmail(request):
    return render(request, 'Gmail.html')
def Photos(request):
    return render(request, 'Photos.html')