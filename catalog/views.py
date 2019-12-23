from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from django.utils.timezone import timedelta, now
from .models import *
from authsys.models import FailedPack
from json import loads, dumps


def index(request):
    count_of_packs = Pack.objects.count()

    return render(request, "index.html",
                  context={"count_of_packs": count_of_packs})


def lol(request):
    return HttpResponse("<ul><li>lol</li><li>kek</li><li>cheburek</li></ul>")


def packs(request):
    request.session['answers'] = None
    request.session['result_list'] = None
    user = request.user
    if user.is_authenticated:
        context = {}
        packs = []
        profile = user.userprofile

        i = 0
        while i < profile.failed_packs.count():
            failed = profile.failed_packs.all()[i]
            print(failed.date)
            print(now())
            if failed.date + timedelta(seconds=20) <= now():
                print(f"Pack reseted for {user.username}")
                profile.failed_packs.remove(failed)
                failed.delete()
                continue
            i += 1

        print([failed.pack for failed in profile.failed_packs.all()])

        for pack in Pack.objects.all():
            if pack not in profile.completed_packs.all() and pack not in [failed.pack for failed in profile.failed_packs.all()]:
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
        if pack in user.userprofile.completed_packs.all() or pack in [failed.pack for failed in user.userprofile.failed_packs.all()]:
            return redirect(reverse("catalog:packs"))

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
            is_correct_answer = answers[i] == questions[i].index_of_correct
            if not is_correct_answer:
                result = False
            result_list.append(is_correct_answer)

        user = request.user
        if result:
            user.userprofile.paisons += pack.reward
            user.userprofile.completed_packs.add(pack)
            user.userprofile.save()
            user.userprofile.check_achievements()
        else:
            try:
                failed = pack.failedpack
                print(f"Failed Pack: {failed.date}")
            except:
                failed = FailedPack.objects.create(pack=pack)
            failed.date = now()
            failed.save()
            user.userprofile.failed_packs.add(failed)
            user.userprofile.save()
        request.session["result_list"] = result_list
        request.session["answers"] = answers
        return HttpResponse(":)")


class Result:
    def __init__(self, question, is_correct, user_answer):
        self.question = question
        self.is_correct = is_correct
        self.user_answer = user_answer


def view_results(request, pack_index):
    result_list = request.session.get('result_list')
    answers = request.session.get('answers')
    pack = Pack.objects.get(id=pack_index)
    questions = pack.question_set.all()

    results = []
    for i in range(len(result_list)):
        answer = answers[i]
        if answer == -1:
            answer = None
        else:
            answer = questions[i].get_answers()[answer]
        results.append(Result(questions[i], result_list[i], answer))

    context = {
        'results': results,
        "result": not (False in result_list)
    }

    return render(
        request,
        'view_results.html',
        context=context
    )
