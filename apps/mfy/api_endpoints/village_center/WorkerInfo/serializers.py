from rest_framework import serializers
from apps.mfy.models import WorkerInfo, WorkerPosition


class WorkerPositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkerPosition
        fields = ("id", "name")


class WorkerInfoListSerializer(serializers.ModelSerializer):
    position = WorkerPositionSerializer()

    class Meta:
        model = WorkerInfo
        fields = (
            "id",
            "position",
            "full_name",
            "photo",
            "about",
            "phone_numbers",
            "work_times",
        )
