from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

def user(request):
    return render(request, 'user.html')

def home(request):
    return HttpResponse("Hello, world! Welcome to Educative$!")