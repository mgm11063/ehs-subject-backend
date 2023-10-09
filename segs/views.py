from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Seg, Factor
from .serializers import FactorOptionSerializer, SegSerializer


class Factors(APIView):
    def get(self, request):
        all_factor = Factor.objects.all()
        serializer = FactorOptionSerializer(
            all_factor,
            many=True,
        )
        return Response(serializer.data)


class Segs(APIView):
    def get(self, request):
        all_seg_type = Seg.objects.all()
        serializer = SegSerializer(
            all_seg_type,
            many=True,
        )
        return Response(serializer.data)
