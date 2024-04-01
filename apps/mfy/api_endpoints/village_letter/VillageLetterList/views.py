from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from apps.mfy.api_endpoints.village_letter.VillageLetterList.serializers import (
    VillageLetterListSerializer,
)


class VillageLetterListAPIView(generics.ListAPIView):
    serializer_class = VillageLetterListSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return self.request.user.village_letters.all()
