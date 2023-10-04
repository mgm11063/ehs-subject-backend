from django.db import models


class SegType(models.Model):

    """SegType Model Definition"""

    name = models.CharField(max_length=80)

    def __str__(self) -> str:
        return self.name


class Staff(models.Model):
    """Staff Definiton"""

    examinationChoices = [
        ("다른병원에서 일반검진", "다른병원에서 일반검진"),
        ("고대에서 일반검진", "고대에서 일반검진"),
        ("센트럴에서 일반검진", "센트럴에서 일반검진"),
    ]
    # 일반 특수 다름

    name = models.CharField(max_length=10)  # 이름
    is_office = models.BooleanField(default=False)  # 사무직 구분

    seg_type = models.ForeignKey(
        SegType, related_name="staffs", on_delete=models.SET_NULL, null=True
    )  # 공정명(SEG)
    g_examination = models.CharField(
        max_length=100,
        choices=examinationChoices,
    )  # 일반검진 실시 여부
    s_examination = models.CharField(
        max_length=100,
        choices=examinationChoices,
    )  # 특수검진 실시 여부

    factors = models.ManyToManyField(
        "factors.Factor",
        related_name="factors",
    )

    is_night = models.BooleanField(default=False)  # 야간근무자
    join_date = models.DateField()  # 입사일
    is_complete = models.BooleanField(default=False)  # 검진완료
    examination_date = models.DateField()  # 차기 검진일

    def __str__(self) -> str:
        return self.name
