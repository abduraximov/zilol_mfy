from rest_framework import generics

from apps.mfy.api_endpoints.village_center.VillageCenter.serializers import VillageCenterSerilizer
from apps.mfy.models import VillageCenter


class VillageCenterAPIView(generics.RetrieveAPIView):
    serializer_class = VillageCenterSerilizer

    def get_object(self):
        return VillageCenter.objects.last()
