from django.db import models
from segs.models import Seg


class G_examination(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.name


class S_examination(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.name


class Staff(models.Model):
    """Staff Definiton"""

    name = models.CharField(max_length=10)  # 이름
    is_office = models.BooleanField(default=False)  # 사무직 구분
    is_night = models.BooleanField(default=False)  # 야간근무자

    g_examination = models.ForeignKey(
        G_examination, related_name="staffs", on_delete=models.SET_NULL, null=True
    )
    s_examination = models.ForeignKey(
        S_examination, related_name="staffs", on_delete=models.SET_NULL, null=True
    )
    join_date = models.DateField()  # 입사&배치일
    pre_examination_date = models.DateField(null=True)  # 배치전 검진일

    segs = models.ForeignKey(
        Seg, related_name="staffs", on_delete=models.CASCADE, null=False
    )

    def __str__(self) -> str:
        return self.name
