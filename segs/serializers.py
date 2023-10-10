from rest_framework import serializers
from .models import Factor, Seg


class FactorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Factor
        fields = ("value", "label", "check_cycle", "regular_check_cycle")


class SegSerializer(serializers.ModelSerializer):
    factors = FactorSerializer(many=True, read_only=True)

    class Meta:
        model = Seg
        fields = ("name", "factors")
