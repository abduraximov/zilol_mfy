from rest_framework import serializers
from apps.mfy.models import VillageInventor


class UserVillageInventorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = VillageInventor
        fields = (
            "full_name",
            "type_of_invention",
            "invention_photo",
            "importance_invention",
        )
