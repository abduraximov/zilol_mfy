from rest_framework import serializers
from apps.mfy.models import VillageLetterQuestions, QuestionAnswerChoice


class QuestionAnswerChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionAnswerChoice
        fields = ("id", "text")


class VillageLetterQuestionsSerializer(serializers.ModelSerializer):
    answer_choices = QuestionAnswerChoiceSerializer(many=True)

    class Meta:
        model = VillageLetterQuestions
        fields = ("id", "type", "text_question", "answer_choices")
