from rest_framework import serializers
from .models import Factor


class FactorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Factor
        fields = ("pk", "value", "check_cycle")


class FactorOptionSerializer(serializers.ModelSerializer):
    read_only_fields = ("check_cycle",)

    class Meta:
        model = Factor
        fields = ("value", "label")
