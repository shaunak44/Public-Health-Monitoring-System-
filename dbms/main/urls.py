from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name="index"),
    path('index/', views.index1, name="index1"),
    path('create/', views.create, name="create"),
    path("register/", views.register, name="register"),
    path("logout/", views.logout_request, name="logout"),
    path("login/", views.login_request, name="login"),
    path("wrong/", views.wrong, name="wrong"),
    path("options/", views.options, name="options"),
    path("citizen/", views.citizenFunction, name="citizenFunction"),
    path("doctor/", views.doctorFunction, name="doctorFunction"),
    path("hospital/", views.hospitalFunction, name="hospitalFunction"),
    path("citizen1/", views.citizen1, name="citizen1"),
    path("confirmation/", views.confirmation, name="confirmation"),
    path("doctor1/", views.doctor1, name="doctor1"),
    path("hospital1/", views.hospital1, name="hospital1"),
    path("hospital2/", views.hospital2, name="hospital2"),
    path("profile/", views.profileFunction, name="profile"),
    path("test/", views.test, name="test"),
    path("stats/", views.stats, name="stats"),
]