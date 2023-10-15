from datetime import datetime, timedelta
from django.db.models import Q
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST
from rest_framework.exceptions import NotFound
from rest_framework import status
from .serializers import StaffSerializer, StaffUpdateSerializer
from .models import Staff
from companies.models import Company
from companies.serializers import (
    CompanyDetailSerializer,
    CompanySerializer,
)


class Staffs(APIView):
    def post(self, request):
        # 여기서 판독
        if isinstance(request.data, dict):
            serializer = StaffSerializer(data=request.data)
        else:
            serializer = StaffSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            # response 수정 여지 있지만 임시로 사용
            return Response()
        else:
            return Response(
                serializer.errors,
                status=HTTP_400_BAD_REQUEST,
            )


class StaffsUpdateAPIView(APIView):
    def get_object(self, pk):
        try:
            company = Company.objects.get(pk=pk)
            companyStaffs = company.staffs.filter(
                pre_examination_date__lte=datetime.now().date()
            )
            print(companyStaffs)
            return companyStaffs
        except Company.DoesNotExist:
            raise NotFound("Company not found or pre_examination_date is not valid.")

    def get(self, request, pk):
        companies = self.get_object(pk)
        serializer = StaffSerializer(companies, many=True)
        return Response(serializer.data)

    def put(self, request, pk):
        updates = request.data
        for update_data in updates:
            pk = update_data.pop("pk")
            Staff.objects.filter(pk=pk).update(**update_data)
        return Response("ok")
