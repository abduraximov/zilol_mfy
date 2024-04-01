from rest_framework import generics

from apps.mfy.api_endpoints.village_businnesmen.VillageBusinnesmenList.serializers import (
    VillageBusinnesmenListSerilizer,
)
from apps.mfy.models import VillageBusinnesmen


class VillageBusinnesmenListAPIView(generics.ListAPIView):
    serializer_class = VillageBusinnesmenListSerilizer
    queryset = VillageBusinnesmen.objects.all()
