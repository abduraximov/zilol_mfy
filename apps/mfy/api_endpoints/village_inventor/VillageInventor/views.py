from rest_framework import generics
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import IsAuthenticated

from apps.mfy.api_endpoints.village_inventor.VillageInventor.serializers import VillageInventorSerilizer


class VillageInventorAPIView(generics.CreateAPIView):
    serializer_class = VillageInventorSerilizer
    permission_classes = (IsAuthenticated, )
    parser_classes = (MultiPartParser, )

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
