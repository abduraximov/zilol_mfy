from rest_framework import serializers
from apps.mfy.models import VillageLetter


class VillageLetterListSerializer(serializers.ModelSerializer):
    class Meta:
        model = VillageLetter
        fields = (
            "id",
            "street",
            "home_number",
            "householder",
            "family_member",
            "home_info",
            "suggestions_problems",
        )
