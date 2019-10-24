from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("lol/", views.lol, name="lol"),
    path("packs/", views.packs, name="packs")
]
