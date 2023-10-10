from rest_framework import serializers
from .models import Staff
from segs.models import Seg
from rest_framework import serializers


class StaffSerializer(serializers.ModelSerializer):
    segs = serializers.SlugRelatedField(
        read_only=False, slug_field="name", queryset=Seg.objects.all()
    )

    class Meta:
        model = Staff
        fields = (
            "pk",
            "name",
            "is_office",
            "g_examination",
            "s_examination",
            "is_night",
            "join_date",
            "examination_date",
            "is_complete",
            "segs",
        )
