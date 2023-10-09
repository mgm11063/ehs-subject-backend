from rest_framework import serializers
from .models import Factor, Seg


class FactorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Factor
        fields = ("pk", "value", "label", "check_cycle", "regular_check_cycle")


class FactorOptionSerializer(serializers.ModelSerializer):
    read_only_fields = ("check_cycle", "regular_check_cycle")

    class Meta:
        model = Factor
        fields = ("name",)


class SegSerializer(serializers.ModelSerializer):
    factors = FactorSerializer(many=True, read_only=True)

    class Meta:
        model = Seg
        fields = ("name", "factors")
