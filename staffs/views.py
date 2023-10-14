from django.core.exceptions import ValidationError
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.status import HTTP_400_BAD_REQUEST
from .serializers import StaffSerializer
from .serializers import StaffSerializer
from .models import Staff


class Staffs(APIView):
    def get_object(self, pk):
        try:
            return Staff.objects.get(pk=pk)
        except Staff.DoesNotExist:
            raise NotFound

    def get(self, request):
        all_staff = Staff.objects.all()
        serializer = StaffSerializer(
            all_staff,
            many=True,
        )
        return Response(serializer.data)

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

    def validate_ids(self, id_list):
        for id in id_list:
            try:
                Staff.objects.get(id=id)
            except (Staff.DoesNotExist, ValidationError):
                raise status.HTTP_400_BAD_REQUEST
        return True

    def put(self, request, *args, **kwargs):
        data = request.data
        ticket_ids = [i["pk"] for i in data]
        self.validate_ids(ticket_ids)
        instances = []
        for staff in data:
            ticket_id = staff["pk"]
            name = staff["name"]
            is_office = staff["is_office"]
            g_examination = staff["g_examination"]
            s_examination = staff["s_examination"]
            join_date = staff["join_date"]
            pre_examination_date = staff["pre_examination_date"]
            segs = staff["segs"]
            obj = self.get_object(ticket_id)
            obj.name = name
            obj.is_office = is_office
            obj.g_examination = g_examination
            obj.s_examination = s_examination
            obj.join_date = pre_examination_date
            obj.description = description
            obj.description = description
            obj.description = description
            obj.save()
            instances.append(obj)
        serializer = StaffSerializer(instances, many=True)
        return Response(serializer.data)
