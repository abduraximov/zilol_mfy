from rest_framework import serializers
from apps.mfy.models import Street


class StreetListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Street
        fields = ("id", "name")
