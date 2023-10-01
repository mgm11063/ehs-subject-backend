from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework.status import HTTP_204_NO_CONTENT
from .models import Company
from .serializers import CompanySerializer, CompanyDetailSerializer


class Companies(APIView):
    def get(self, request):
        all_company = Company.objects.all()
        serializer = CompanySerializer(
            all_company,
            many=True,
        )
        return Response(serializer.data)


class CompanyDetail(APIView):
    def get_object(self, pk):
        try:
            return Company.objects.get(pk=pk)
        except Company.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        company = self.get_object(pk)
        serializer = CompanyDetailSerializer(
            company,
            context={"request": request},
        )
        return Response(serializer.data)

    # def put(self, request, pk):
    #     room = self.get_object(pk)
    #     if room.owner != request.user:
    #         raise PermissionDenied
    #     # your magic

    def delete(self, request, pk):
        room = self.get_object(pk)
        room.delete()
        return Response(status=HTTP_204_NO_CONTENT)
