from rest_framework import generics
from apps.mfy.api_endpoints.jobseeker.JobSeeker.serializers import JobSeekerSerializer
from rest_framework.permissions import IsAuthenticated


class JobSeekerCreateAPIView(generics.CreateAPIView):
    serializer_class = JobSeekerSerializer
    permission_classes = (IsAuthenticated,)
