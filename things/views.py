from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    response = HttpResponse('Welcome to things!')
    return response
# Create your views here.
