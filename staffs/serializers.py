from rest_framework import serializers
from .models import Staff, G_examination, S_examination
from segs.models import Seg
from segs.serializers import SegSerializer
from opinions.serializers import OpinionSerializer
from rest_framework import serializers


class GExaminationSerializer(serializers.ModelSerializer):
    class Meta:
        model = G_examination
        fields = "__all__"


class SExaminationSerializer(serializers.ModelSerializer):
    class Meta:
        model = S_examination
        fields = "__all__"


class StaffSerializer(serializers.ModelSerializer):
    segs = SegSerializer()
    opinions = OpinionSerializer()

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
            "pre_examination_date",
            "segs",
            "opinions",
        )

    def create(self, validated_data):
        seg_data = validated_data.pop("segs")
        seg_instance = Seg.objects.get(name=seg_data["name"])
        instance = Staff.objects.create(segs=seg_instance, **validated_data)

        return instance


class StaffUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = ("pre_examination_date",)


class StaffDashbordSerializer(serializers.ModelSerializer):
    segs = SegSerializer()
    opinions = OpinionSerializer()

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
            "pre_examination_date",
            "segs",
            "opinions",
        )
