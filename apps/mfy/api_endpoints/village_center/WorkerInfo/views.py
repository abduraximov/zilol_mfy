from rest_framework import generics

from apps.mfy.api_endpoints.village_center.WorkerInfo.serializers import (
    WorkerInfoListSerializer,
)
from apps.mfy.models import WorkerInfo


class WorkerInfoListAPIView(generics.ListAPIView):
    serializer_class = WorkerInfoListSerializer
    queryset = WorkerInfo.objects.all()
