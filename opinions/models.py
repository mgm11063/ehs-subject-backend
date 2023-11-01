from django.core.validators import RegexValidator
from django.db import models


class Opinion(models.Model):
    year_and_month = models.CharField(
        max_length=7,
        validators=[
            RegexValidator(
                regex=r"^\d{4}-\d{2}$",
                message="Year and month should be in YYYY-MM format.",
                code="invalid_year_month",
            ),
        ],
    )
    opinion = models.TextField(max_length=999)

    def __str__(self) -> str:
        return self.opinion
