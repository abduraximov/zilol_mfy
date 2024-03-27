from rest_framework import serializers
from apps.mfy.models import JobSeeker


class JobSeekerSerializer(serializers.ModelSerializer):

    class Meta:
        model = JobSeeker
        fields = (
            "id",
            "home_number",
            "address",
            "full_name",
            "specialist",
            "phone_number",
        )
