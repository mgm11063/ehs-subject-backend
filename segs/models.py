from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Factor(models.Model):
    value = models.CharField(
        max_length=100,
    )
    label = models.CharField(max_length=100, editable=False)
    check_cycle = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(12)],
        null=True,
        default=0,
        blank=True,
    )
    regular_check_cycle = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(24)],
        null=True,
        default=0,
        blank=True,
    )

    def __str__(self) -> str:
        return self.value

    def save(self, *args, **kwargs):
        self.label = self.value
        super(Factor, self).save(*args, **kwargs)


class Seg(models.Model):

    """Seg Model Definition"""

    name = models.CharField(max_length=80)
    factors = models.ManyToManyField(Factor, related_name="segs", null=True, blank=True)

    def __str__(self) -> str:
        return self.name

    def once_cycle_date(self):
        check_cycles = [
            factor.check_cycle
            for factor in self.factors.all()
            if factor.check_cycle is not None
        ]

        if not check_cycles:
            return None

        min_check_cycle = min(check_cycles)
        return min_check_cycle

    def regular_cycle_date(self):
        regular_check_cycles = [
            factor.regular_check_cycle
            for factor in self.factors.all()
            if factor.regular_check_cycle is not None
        ]

        if not regular_check_cycles:
            return None

        min_regular_check_cycle = min(regular_check_cycles)
        return min_regular_check_cycle
