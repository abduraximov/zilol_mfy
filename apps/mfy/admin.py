from django.contrib import admin
from .models import (
    VillageCenter,
    WorkerPosition,
    WorkerInfo,
    Street,
    VillageLetter,
    VillageLetterQuestions,
    QuestionAnswerChoice,
    VillageInventor,
    VillageBusinnesmen,
    VillageBusinnesmenProduct,
    JobSeeker,
)


@admin.register(VillageCenter)
class VillageCenterAdmin(admin.ModelAdmin):
    list_display = ("name", "location", "phone_number")
    search_fields = ("name",)


@admin.register(WorkerPosition)
class WorkerPositionAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(WorkerInfo)
class WorkerInfoAdmin(admin.ModelAdmin):
    list_display = ("position", "full_name", "created_at")
    list_filter = ("position",)


@admin.register(Street)
class StreetAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(VillageLetter)
class VillageLetterAdmin(admin.ModelAdmin):
    list_display = (
        "street",
        "home_number",
        "householder",
        "family_member",
        "home_info",
        "suggestions_problems",
    )
    search_fields = ("home_number", "householder")


class WorkerInfoInline(admin.TabularInline):
    model = QuestionAnswerChoice
    extra = 0


@admin.register(VillageLetterQuestions)
class VillageLetterQuestionsAdmin(admin.ModelAdmin):
    list_display = ("type", "text_question")
    inlines = [WorkerInfoInline]


@admin.register(VillageInventor)
class VillageInventorAdmin(admin.ModelAdmin):
    list_display = ("full_name", "type_of_invention")


@admin.register(VillageBusinnesmen)
class VillageBusinnesmenAdmin(admin.ModelAdmin):
    list_display = ("legal_name", "phone_number")


@admin.register(VillageBusinnesmenProduct)
class VillageBusinnesmenProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price")


@admin.register(JobSeeker)
class JobSeekerAdmin(admin.ModelAdmin):
    list_display = ("home_number", "address", "full_name")
