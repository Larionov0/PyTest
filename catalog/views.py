from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from django.db.models import QuerySet
from .models import *
from authsys.models import IncorrectPack as FailedPack
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
        packs = []
        profile = user.userprofile
        for pack in Pack.objects.all():
            if pack not in profile.completed_packs.all() and pack not in profile.failed_packs.all():
                packs.append(pack)

        context["completed_count"] = profile.completed_packs.count()
        context["all_packs"] = packs
        context["username"] = user.username
        context["paisons"] = profile.paisons
        context["achievements"] = profile.achievements.all()

        return render(request, "MyCabinet_page.html", context=context)
    else:
        return redirect("/auth/login/")


def pack(request, pack_index):
    try:
        pack = Pack.objects.get(id=pack_index)
    except:
        return Http404("Pack not found ‿︵‿ヽ(°□° )ノ︵‿︵")

    user = request.user
    if user.is_authenticated:
        if pack in user.userprofile.completed_packs.all() or pack in user.userprofile.failed_packs.all():
            return redirect(reverse("packs"))

        return render(request,
                  "Pack_page.html",
                  context={
                      "pack": pack,
                  })
    else:
        return redirect(reverse("authsys:login"))


def end_test(request, pack_index):
    try:
        pack = Pack.objects.get(id=pack_index)
    except:
        return Http404("Pack not found ‿︵‿ヽ(°□° )ノ︵‿︵")

    if request.POST:
        answers = loads(request.POST["answers"])
        questions = pack.question_set.all()
        result_list = []
        result = True
        for i in range(len(answers)):
            """
            Here I need to check answers and add result
            to database! Also I need to refresh Paisons
            of that user in positive case.
            """
            is_correct_answer = answers[i] == questions[i].index_of_correct
            if not is_correct_answer:
                result = False
            result_list.append(is_correct_answer)

        user = request.user
        if result:
            user.userprofile.paisons += pack.paisons
            user.userprofile.completed_packs.add(pack)
        else:
            FailedPack.objects.create(name=pack.name,)

        return HttpResponse(dumps(result_list))
