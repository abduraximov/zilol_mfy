from rest_framework import generics

from apps.mfy.api_endpoints.village_letter.Street.serializers import (
    StreetListSerializer,
)
from apps.mfy.models import Street


class StreetListAPIView(generics.ListAPIView):
    serializer_class = StreetListSerializer
    queryset = Street.objects.all()
