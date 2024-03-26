from rest_framework import generics

from apps.mfy.api_endpoints.village_inventor.VillageInventorList.serializers import VillageInventorListSerilizer
from apps.mfy.models import VillageInventor


class VillageInventorListAPIView(generics.ListAPIView):
    serializer_class = VillageInventorListSerilizer
    queryset = VillageInventor.objects.all()