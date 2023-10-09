from django.urls import path
from . import views

urlpatterns = [
    path("", views.Staffs.as_view()),
]
