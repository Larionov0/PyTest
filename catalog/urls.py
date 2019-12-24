from django.urls import path
from . import views

app_name = "catalog"

urlpatterns = [
    path("", views.index, name="index"),
    path("packs/", views.packs, name="packs"),
    path("packs/<int:pack_index>/", views.pack, name="pack"),
    path("packs/<int:pack_index>/end_test", views.end_test, name="end_test"),
    path("packs/<int:pack_index>/view_results", views.view_results, name="view_results")
]
