from rest_framework import serializers
from apps.mfy.models import VillageBusinnesmen, VillageBusinnesmenProduct
from django.utils.translation import gettext_lazy as _


class VillageBusinnesmenSerilizer(serializers.ModelSerializer):
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
        )


class VillageBusinnesmenProductSerilizer(serializers.ModelSerializer):
    village_businnesmen_id = serializers.IntegerField(required=True)

    class Meta:
        model = VillageBusinnesmenProduct
        fields = ("id", "name", "photo", "price", "village_businnesmen_id")

    def validate_village_businnesmen_id(self, value):
        user = self.context["request"].user
        if not VillageBusinnesmen.objects.filter(id=value, owner=user).exists():
            raise serializers.ValidationError(
                detail={
                    "village_businnesmen_id": _("You can't add product to this village businnesmen."),
                    "error": _("invalid_pk_or_owner")
                },
                code="invalid_pk_or_owner"
            )
        return value