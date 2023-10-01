from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Factor(models.Model):
    name = models.CharField(max_length=100)  # 이름
    check_cycle = models.IntegerField(
        validators=[
            MinValueValidator(0),
        ]
    )  # 검진주기

    def __str__(self) -> str:
        return self.name
