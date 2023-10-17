from django.urls import path
from . import views
from staffs.views import StaffsUpdateAPIView, StaffDashbord

urlpatterns = [
    path("", views.Companies.as_view()),
    path("<int:pk>", views.CompanyDetail.as_view()),
    path("<int:pk>/staffs", StaffsUpdateAPIView.as_view()),
    path("<int:pk>/dashbord", StaffDashbord.as_view()),
]
