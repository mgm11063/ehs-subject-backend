from rest_framework import serializers
from .models import Staff
from segs.models import Seg
from segs.serializers import SegSerializer


class StaffSerializer(serializers.ModelSerializer):
    segs = SegSerializer(read_only=True)
    read_only_fields = ("examination_date",)

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
            "is_complete",
            "segs",
        )
