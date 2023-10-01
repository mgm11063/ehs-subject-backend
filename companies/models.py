from django.db import models
from common.models import CommonModel


class Company(CommonModel):
    """Company Definiton"""

    name = models.CharField(
        max_length=150,
        default="",
    )

    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="companys",
    )
    staffs = models.ManyToManyField(
        "staffs.Staff",
        related_name="companys",
    )

    def __str__(self) -> str:
        return self.name
