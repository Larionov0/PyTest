from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from django.db.models import QuerySet
from .models import *
from json import loads, dumps


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
    user = request.user
    if user.is_authenticated:
        context = {}
        count_of_packs = Pack.objects.count()
        packs = []
        profile = user.userprofile
        for pack in Pack.objects.all():
            if pack not in profile.completed_packs.all():
                packs.append(pack)

        context["completed_count"] = profile.completed_packs.count()
        context["all_packs"] = packs
        context["username"] = user.username
        context["paisons"] = profile.paisons

        return render(request, "MyCabinet_page.html", context=context)
    else:
        return redirect("/auth/login/")


def pack(request, pack_index):
    try:
        pack = Pack.objects.get(id=pack_index)
    except:
        return Http404("Pack not found ‿︵‿ヽ(°□° )ノ︵‿︵")

    return render(request,
                  "Pack_page.html",
                  context={
                      "pack": pack,
                  })


def end_test(request, pack_index):
    try:
        pack = Pack.objects.get(id=pack_index)
    except:
        return Http404("Pack not found ‿︵‿ヽ(°□° )ノ︵‿︵")

    if request.POST:
        answers = loads(request.POST["answers"])
        questions = pack.question_set.all()
        result_list = []
        for i in range(len(answers)):
            """
            Here I need to check answers and add result
            to database! Also I need to refresh Paisons
            of that user in positive case.
            """
            result_list.append(answers[i] == questions[i].index_of_correct)

        return HttpResponse(dumps(result_list))
