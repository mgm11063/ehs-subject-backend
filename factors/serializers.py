from rest_framework import serializers
from .models import Factor


class FactorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Factor
        fields = ("pk", "name", "check_cycle")


class FactorOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Factor
        fields = ("name",)
