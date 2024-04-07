from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from apps.mfy.models import VillageInventor
from apps.mfy.api_endpoints.village_inventor.UserVillageInventors.serializers import UserVillageInventorsSerializer


class UserVillageInventorsAPIView(generics.ListAPIView):
    serializer_class = UserVillageInventorsSerializer
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        user = self.request.user
        return VillageInventor.objects.filter(owner_id=user.id)