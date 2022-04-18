from django.shortcuts import render
from django.http import HttpResponse



# Create your views here.

def index(request):
    return HttpResponse("Greetings Human, you have just read me.")