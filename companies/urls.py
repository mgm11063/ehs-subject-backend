from django.urls import path
from . import views

urlpatterns = [
    path("", views.Companies.as_view()),
    path("<int:pk>", views.CompanyDetail.as_view()),
]
