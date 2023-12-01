from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST
from rest_framework.views import APIView
from .serializers import OpinionSerializer


class Opinions(APIView):
    def post(self, request):
        serializer = OpinionSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            # response 수정 여지 있지만 임시로 사용
            return Response()
        else:
            return Response(
                serializer.errors,
                status=HTTP_400_BAD_REQUEST,
            )
