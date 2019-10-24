from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import *


# Create your views here.
def index(request):
    count_of_packs = Pack.objects.all().count()
    count_of_questions = Question.objects.all().count()
    return render(request, "index.html",
                  context={"count of packs": count_of_packs,
                           "count of questions": count_of_questions})


def lol(request):
    return HttpResponse("<ul><li>lol</li><li>kek</li><li>cheburek</li></ul>")
