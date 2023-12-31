from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/companies/", include("companies.urls")),
    path("api/v1/staffs/", include("staffs.urls")),
    path("api/v1/segs/", include("segs.urls")),
    path("api/v1/opinions/", include("opinions.urls")),
]
