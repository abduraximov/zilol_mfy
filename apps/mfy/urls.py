from django.urls import path
from apps.mfy.api_endpoints import village_center, village_letter, village_inventor, village_businnesmen, jobseeker

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
    path(
        "VillageBusinnesmen/",
        village_businnesmen.VillageBusinnesmenAPIView.as_view(),
        name="VillageBusinnesmen"
    ),
    path(
        "VillageBusinnesmenProduct/",
        village_businnesmen.VillageBusinnesmenProductAPIView.as_view(),
        name="VillageBusinnesmenProduct"
    ),
    path(
        "VillageBusinnesmenList/",
        village_businnesmen.VillageBusinnesmenListAPIView.as_view(),
        name="VillageBusinnesmenList"
    ),
    path("JobSeekerCreate/", jobseeker.JobSeekerCreateAPIView.as_view(), name="JobSeekerCreate"),

]
