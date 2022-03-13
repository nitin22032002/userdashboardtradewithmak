from django.urls import path
from . import views

urlpatterns=[
    path("adduser/",views.addUserPage),
    path("add/user",views.addUser),
    path("show/user/",views.showUser)
]