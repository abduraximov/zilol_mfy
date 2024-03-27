from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from apps.mfy.api_endpoints.village_businnesmen.VillageBusinnesmenList.serializers import \
    VillageBusinnesmenListSerilizer
from apps.mfy.models import VillageBusinnesmen


class VillageBusinnesmenListAPIView(generics.ListAPIView):
    serializer_class = VillageBusinnesmenListSerilizer
    permission_classes = (IsAuthenticated, )
    queryset = VillageBusinnesmen.objects.all()

