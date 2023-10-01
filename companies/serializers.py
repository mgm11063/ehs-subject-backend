from rest_framework import serializers
from staffs.serializers import StaffSerializer
from .models import Company


class CompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = (
            "pk",
            "name",
            "user",
        )


class CompanyDetailSerializer(serializers.ModelSerializer):
    staffs = StaffSerializer(many=True, read_only=True)

    class Meta:
        model = Company
        fields = (
            "staffs",
        )
