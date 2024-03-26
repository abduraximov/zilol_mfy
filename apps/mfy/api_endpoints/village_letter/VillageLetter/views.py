from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from apps.mfy.api_endpoints.village_letter.VillageLetter.serializers import VillageLetterSerializer


class VillageLetterAPIView(generics.CreateAPIView):
    serializer_class = VillageLetterSerializer
    permission_classes = (IsAuthenticated, )

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
