from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("lol/", views.lol, name="lol"),
    path("packs/", views.packs, name="packs"),
    path("packs/<int:pack_index>/", views.pack, name="pack"),
    path("packs/<int:pack_index>/end_test", views.end_test, name="end_test")
]
