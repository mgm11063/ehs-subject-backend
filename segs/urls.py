from django.urls import path
from . import views

urlpatterns = [
    path("", views.Segs.as_view()),
    path("<int:pk>", views.SegDetail.as_view()),
    path("factors", views.Factors.as_view()),
]
