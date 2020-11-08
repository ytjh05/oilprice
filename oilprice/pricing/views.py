from .models import Position
from rest_framework import viewsets, permissions
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import PositionSerialize
from haversine import haversine, Unit

class PositionViewSet(viewsets.ModelViewSet):
    queryset = Position.objects.all().order_by('name')
    serializer_class = PositionSerialize
    permission_classes = [permissions.IsAuthenticated]
class PositionInfo(APIView):
    def get(self, request):
        long = float(request.GET.get('longitude', None))
        lat = float(request.GET.get('latitude', None))
        pos = (lat, long)
        latitude__range=(lat - 0.01, lat + 0.01)
        longitude__range=(long - 0.015, long + 0.015)
# Create your views here.
