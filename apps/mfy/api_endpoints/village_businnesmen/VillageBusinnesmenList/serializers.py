from rest_framework import serializers
from apps.mfy.models import VillageBusinnesmen, VillageBusinnesmenProduct


class VillageBusinnesmenProductListSerilizer(serializers.ModelSerializer):

    class Meta:
        model = VillageBusinnesmenProduct
        fields = ("id", "name", "photo", "price")


class VillageBusinnesmenListSerilizer(serializers.ModelSerializer):
    products = VillageBusinnesmenProductListSerilizer(many=True)

    class Meta:
        model = VillageBusinnesmen
        fields = (
            "id",
            "legal_name",
            "phone_number",
            "certificate_photo",
            "address",
            "latitude",
            "longitude",
            "products",
        )

