from django.urls import path
from . import views

app_name = "authsys"

urlpatterns = [
    path(r"login/", views.login, name="login"),
    path(r'logout/', views.logout, name="logout"),
    path(r'signup', views.RegisterFormView.as_view(), name="signup")
]
