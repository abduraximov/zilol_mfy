from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.common.models import TimeStampedModel


class VillageCenter(TimeStampedModel):
    name = models.CharField(_("Name"), max_length=256)
    location = models.CharField(_("Location"), max_length=512, blank=True, null=True)
    phone_number = models.CharField(
        _("Phone Number"), max_length=20, blank=True, null=True
    )

    class Meta:
        verbose_name = _("Village Center")
        verbose_name_plural = _("Village Centers")

    def __str__(self):
        return self.name


class WorkerPosition(TimeStampedModel):
    name = models.CharField(_("Name"), max_length=256)

    class Meta:
        verbose_name = _("Worker Position")
        verbose_name_plural = _("Worker Positions")

    def __str__(self):
        return self.name


class WorkerInfo(TimeStampedModel):
    position = models.ForeignKey(
        "mfy.WorkerPosition",
        verbose_name=_("Position"),
        on_delete=models.CASCADE,
        null=True,
    )
    full_name = models.CharField(_("Full name"), max_length=512)
    photo = models.ImageField(
        _("Photo"), upload_to="workers_photo", null=True, blank=True
    )
    about = models.TextField(_("About"), null=True, blank=True)
    phone_numbers = models.CharField(
        _("Phone numbers"), max_length=512, null=True, blank=True
    )
    work_times = models.CharField(
        _("Working times"), max_length=512, null=True, blank=True
    )

    class Meta:
        verbose_name = _("Worker Info")
        verbose_name_plural = _("Worker Information")

    def __str__(self):
        return self.full_name


class Street(TimeStampedModel):
    name = models.CharField(_("Name"), max_length=256)

    class Meta:
        verbose_name = _("Street")
        verbose_name_plural = _("Streets")

    def __str__(self):
        return self.name


class VillageLetter(TimeStampedModel):
    street = models.ForeignKey(
        "mfy.Street", verbose_name=_("Street"), on_delete=models.CASCADE, null=True
    )
    home_number = models.CharField(_("Home number"), max_length=256)
    householder = models.TextField(_("Householder"))
    family_member = models.TextField(_("Family member"))
    home_info = models.TextField(_("Home info"))
    suggestions_problems = models.TextField(_("Suggestions and problems"))
    owner = models.ForeignKey(
        "users.User",
        verbose_name=_("Owner"),
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="village_letters",
    )

    class Meta:
        verbose_name = _("Village Letter")
        verbose_name_plural = _("Village Letters")

    def __str__(self):
        return self.home_number


class QuestionType(models.TextChoices):
    HOUSEHOLDER = "HOUSEHOLDER", _("Householder")
    FAMILY_MEMBER = "FAMILY_MEMBER", _("Family member")
    HOME_INFO = "HOME_INFO", _("Home info")
    SUGGESTION_PROBLEM = "SUGGESTION_PROBLEM", _("Suggestion problem")


class VillageLetterQuestions(TimeStampedModel):
    type = models.CharField(_("Type"), choices=QuestionType.choices, max_length=20)
    text_question = models.TextField(_("Text question"))

    class Meta:
        verbose_name = _("Village Letter Question")
        verbose_name_plural = _("Village Letter Questions")

    def __str__(self):
        return self.type


class QuestionAnswerChoice(TimeStampedModel):
    question = models.ForeignKey(
        "mfy.VillageLetterQuestions",
        verbose_name=_("Question"),
        on_delete=models.CASCADE,
        null=True,
        related_name="answer_choices",
    )
    text = models.TextField(_("Text"))

    class Meta:
        verbose_name = _("Question Answer Choice")
        verbose_name_plural = _("Question Answer Choices")

    def __str__(self):
        return self.text


class VillageInventor(TimeStampedModel):
    full_name = models.CharField(_("Full name"), max_length=512)
    type_of_invention = models.CharField(
        _("Type of invention"), max_length=256, null=True, blank=True
    )
    invention_photo = models.ImageField(
        _("Invetion photo"), upload_to="invention_photo", null=True, blank=True
    )
    importance_invention = models.TextField(
        _("Importance invention"), null=True, blank=True
    )
    owner = models.ForeignKey(
        "users.User",
        verbose_name=_("Owner"),
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="village_inventor",
    )

    class Meta:
        verbose_name = _("Village Inventor")
        verbose_name_plural = _("Village Inventors")

    def __str__(self):
        return self.full_name


class VillageBusinnesmen(TimeStampedModel):
    legal_name = models.CharField(_("Legal name"), max_length=512, null=True)
    phone_number = models.CharField(
        _("Phone number"), max_length=512, null=True, blank=True
    )
    certificate_photo = models.ImageField(
        _("Certificate photo"), upload_to="certificate_photo"
    )
    address = models.CharField(_("Address"), max_length=512, null=True, blank=True)
    latitude = models.DecimalField(
        max_digits=9, decimal_places=6, null=True, blank=True
    )
    longitude = models.DecimalField(
        max_digits=9, decimal_places=6, null=True, blank=True
    )
    owner = models.ForeignKey(
        "users.User",
        verbose_name=_("Owner"),
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = _("Village Businnesmen")
        verbose_name_plural = _("Village Businnesmens")

    def __str__(self):
        return self.legal_name


class VillageBusinnesmenProduct(TimeStampedModel):
    name = models.CharField(_("Name"), max_length=512, null=True)
    photo = models.ImageField(
        _("Photo"), upload_to="product_photo", null=True, blank=True
    )
    price = models.CharField(_("Price"), max_length=128, null=True, blank=True)
    village_businnesmen = models.ForeignKey(
        "mfy.VillageBusinnesmen",
        verbose_name=_("Village Businnesmen"),
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="products",
    )

    class Meta:
        verbose_name = _("Village Businnesmen Product")
        verbose_name_plural = _("Village Businnesmen Products")

    def __str__(self):
        return self.name


class JobSeeker(TimeStampedModel):
    home_number = models.CharField(_("Home number"), max_length=256)
    address = models.TextField(_("Address"), null=True, blank=True)
    full_name = models.CharField(_("Full name"), max_length=512, null=True, blank=True)
    specialist = models.CharField(
        _("Specialist"), max_length=512, null=True, blank=True
    )
    phone_number = models.CharField(
        _("Phone number"), max_length=512, null=True, blank=True
    )

    class Meta:
        verbose_name = _("Job Seeker")
        verbose_name_plural = _("Job Seekers")

    def __str__(self):
        return self.home_number
