from rest_framework import generics
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import IsAuthenticated

from apps.mfy.api_endpoints.village_inventor.VillageInventorUpdate.serializers import (
    VillageInventorUpdateSerializer,
)


class VillageInventorUpdateAPIView(generics.UpdateAPIView):
    serializer_class = VillageInventorUpdateSerializer
    permission_classes = (IsAuthenticated,)
    parser_classes = (MultiPartParser,)
    http_method_names = ("put",)

    def get_queryset(self):
        return self.request.user.village_inventor.all()
