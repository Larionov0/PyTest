from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import *


# Create your views here.
def index(request):
    count_of_packs = Pack.objects.all().count()
    packs = Pack.objects.all()
    count_of_questions = Question.objects.all().count()
    questions = Question.objects.all()

    return render(request, "index.html",
                  context={"count_of_packs": count_of_packs,
                           "count_of_questions": count_of_questions,
                           "packs": packs,
                           "questions": questions})


def lol(request):
    return HttpResponse("<ul><li>lol</li><li>kek</li><li>cheburek</li></ul>")


def packs(request):
    count_of_packs = Pack.objects.all().count()
    packs = Pack.objects.all()
    print(request.readline())
    print(dir(request))

    return render(request, "MyCabinet_page.html",
                  context={"count_of_packs": count_of_packs,
                           "all_packs": packs})


def pack(request):
    pack = ""
