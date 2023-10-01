from django.db import models


class CommonModel(models.Model):

    """Common Model Definition"""

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class CommonCommunityModel(models.Model):

    """Common Community Model / name length['80'] limit"""

    CommunityCategoryChoices = [
        ("test", "test1"),
    ]
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    title = models.CharField(max_length=100)
    content = models.TextField(max_length=999)
    category = models.CharField(
        max_length=20,
        choices=CommunityCategoryChoices,
    )

    class Meta:
        abstract = True

    def __str__(self) -> str:
        return self.title
