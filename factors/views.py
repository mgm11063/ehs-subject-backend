from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Factor
from .serializers import FactorOptionSerializer


# Create your views here.
class Factors(APIView):
    def get(self, request):
        all_factor = Factor.objects.all()
        serializer = FactorOptionSerializer(
            all_factor,
            many=True,
        )
        return Response(serializer.data)
