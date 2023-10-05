from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST
from .serializers import StaffSerializer, SegTypeSerializer
from .models import SegType


class Staffs(APIView):
    def post(self, request):
        if isinstance(request.data, dict):
            serializer = StaffSerializer(data=request.data)
        else:
            serializer = StaffSerializer(data=request.data, many=True)

        if serializer.is_valid():
            serializer.save()
            # response 수정 여지 있지만 임시로 사용
            return Response()
        else:
            return Response(
                serializer.errors,
                status=HTTP_400_BAD_REQUEST,
            )


class Segs(APIView):
    def get(self, request):
        all_seg_type = SegType.objects.all()
        serializer = SegTypeSerializer(
            all_seg_type,
            many=True,
        )
        return Response(serializer.data)
