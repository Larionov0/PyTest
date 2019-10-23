from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("<a href = ''>lol</a>")

def lol(request):
    return HttpResponse("<ul><li>lol</li><li>kek</li><li>cheburek</li></ul>")
