from django.urls import path
from . import views

urlpatterns = [
    path("", views.Factors.as_view()),
]
