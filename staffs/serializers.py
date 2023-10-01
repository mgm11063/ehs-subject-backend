from rest_framework import serializers
from .models import Staff, SegType
from factors.serializers import FactorSerializer


class SegTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SegType
        fields = ("name",)


class StaffSerializer(serializers.ModelSerializer):
    seg_type = SegTypeSerializer(read_only=True)
    factors = FactorSerializer(many=True, read_only=True)

    class Meta:
        model = Staff
        fields = (
            "pk",
            "name",
            "is_office",
            "seg_type",
            "g_examination",
            "s_examination",
            "factors",
            "is_night",
            "join_date",
            "is_complete",
            "examination_date",
        )
