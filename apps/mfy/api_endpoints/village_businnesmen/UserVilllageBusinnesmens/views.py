from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from apps.mfy.api_endpoints.village_businnesmen.UserVilllageBusinnesmens.serializers import \
    UserVillageBusinnesmensSerilizer
from apps.mfy.models import VillageBusinnesmen


class UserVillageBusinnesmensAPIView(generics.ListAPIView):
    serializer_class = UserVillageBusinnesmensSerilizer
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        user = self.request.user
        return VillageBusinnesmen.objects.filter(owner_id=user.id)
