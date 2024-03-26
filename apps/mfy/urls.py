from django.urls import path
from apps.mfy.api_endpoints import village_center, village_letter, village_inventor

urlpatterns = [
    path("VillageCenter/", village_center.VillageCenterAPIView.as_view(), name="VillageCenter"),
    path("WorkerInfoList/", village_center.WorkerInfoListAPIView.as_view(), name="WorkerInfoList"),
    path("StreetList/", village_letter.StreetListAPIView.as_view(), name="StreetList"),
    path("VillageLetter/", village_letter.VillageLetterAPIView.as_view(), name="VillageLetter"),
    path("VillageLetterList/", village_letter.VillageLetterListAPIView.as_view(), name="VillageLetterList"),
    path(
        "VillageLetterQuestions/",
        village_letter.VillageLetterQuestionsAPIView.as_view(),
        name="VillageLetterQuestions"
    ),
    path("VillageInventor/", village_inventor.VillageInventorAPIView.as_view(), name="VillageInventor"),
    path(
        "VillageInventorUpdate/<int:pk>/",
        village_inventor.VillageInventorUpdateAPIView.as_view(),
        name="VillageInventorUpdate"
    ),
    path(
        "VillageInventorList/",
        village_inventor.VillageInventorListAPIView.as_view(),
        name="VillageInventorList"
    ),

]
