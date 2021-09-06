from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name = 'aec-index-page'),
    path("login/", views.login, name='aec-login')

]
