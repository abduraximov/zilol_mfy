from rest_framework import generics
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import IsAuthenticated

from apps.mfy.api_endpoints.village_businnesmen.VillageBusinnesmen.serializers import (
    VillageBusinnesmenSerilizer, VillageBusinnesmenProductSerilizer
)


class VillageBusinnesmenAPIView(generics.CreateAPIView):
    serializer_class = VillageBusinnesmenSerilizer
    permission_classes = (IsAuthenticated, )
    parser_classes = (MultiPartParser, )

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class VillageBusinnesmenProductAPIView(generics.CreateAPIView):
    serializer_class = VillageBusinnesmenProductSerilizer
    permission_classes = (IsAuthenticated, )
    parser_classes = (MultiPartParser, )

