from django.urls import path
from . import views


urlpatterns = [
    path(r"login/", views.login, name="login"),
    path(r'logout/', views.logout, name="logout")
]
