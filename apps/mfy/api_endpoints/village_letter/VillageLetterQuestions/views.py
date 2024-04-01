from rest_framework import generics
from apps.mfy.api_endpoints.village_letter.VillageLetterQuestions.serializers import (
    VillageLetterQuestionsSerializer,
)
from apps.mfy.models import VillageLetterQuestions


class VillageLetterQuestionsAPIView(generics.ListAPIView):
    serializer_class = VillageLetterQuestionsSerializer
    queryset = VillageLetterQuestions.objects.all()
