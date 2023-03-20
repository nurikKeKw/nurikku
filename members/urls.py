from django.forms import URLInput
from django.urls import path
from . import views

urlpatterns = [
    path('members', views.members, name='members'),
]