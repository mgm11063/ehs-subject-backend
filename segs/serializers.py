from rest_framework import serializers
from .models import Factor, Seg


class FactorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Factor
        fields = ("value", "label", "check_cycle", "regular_check_cycle")


class SegSerializer(serializers.ModelSerializer):
    factors = FactorSerializer(many=True, read_only=True)
    once_cycle_date = serializers.SerializerMethodField()
    regular_cycle_date = serializers.SerializerMethodField()

    class Meta:
        model = Seg
        fields = ("pk", "name", "factors", "once_cycle_date", "regular_cycle_date")

    def get_once_cycle_date(self, seg):
        return seg.once_cycle_date()

    def get_regular_cycle_date(self, seg):
        return seg.regular_cycle_date()
