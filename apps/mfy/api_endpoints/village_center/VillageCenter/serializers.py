from rest_framework import serializers
from apps.mfy.models import VillageCenter


class VillageCenterSerilizer(serializers.ModelSerializer):
    class Meta:
        model = VillageCenter
        fields = ("id", "name", "location", "phone_number")
