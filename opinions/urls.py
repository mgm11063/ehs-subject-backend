from django.urls import path
from . import views

urlpatterns = [
    path("", views.Opinions.as_view()),
]
