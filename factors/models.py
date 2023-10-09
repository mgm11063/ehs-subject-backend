from django.db import models
from django.core.validators import MinValueValidator


class Factor(models.Model):
    value = models.CharField(
        max_length=100,
    )
    label = models.CharField(max_length=100, editable=False)
    check_cycle = models.IntegerField(
        validators=[MinValueValidator(0)], null=True, default=0, blank=True
    )  # 검진주기

    def __str__(self) -> str:
        return self.value

    def save(self, *args, **kwargs):
        self.label = self.value
        super(Factor, self).save(*args, **kwargs)
