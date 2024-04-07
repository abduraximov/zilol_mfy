from rest_framework import serializers

from apps.mfy.api_endpoints.village_businnesmen.VillageBusinnesmenList.serializers import \
    VillageBusinnesmenProductListSerilizer
from apps.mfy.models import VillageBusinnesmen


class UserVillageBusinnesmensSerilizer(serializers.ModelSerializer):
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
