from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from .models import Seg, Factor
from .serializers import FactorSerializer, SegSerializer


class Factors(APIView):
    def get(self, request):
        all_factor = Factor.objects.all()
        serializer = FactorSerializer(
            all_factor,
            many=True,
        )
        return Response(serializer.data)


class Segs(APIView):
    def get(self, request):
        all_seg_type = Seg.objects.all()
        return Response(all_seg_type.data)


class SegDetail(APIView):
    def get_object(self, pk):
        try:
            return Seg.objects.get(pk=pk)
        except Seg.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        company = self.get_object(pk)
        serializer = SegSerializer(
            company,
            context={"request": request},
        )
        return Response(serializer.data)
