import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField

from apps.common.models import TimeStampedModel
from apps.users.managers import UserManager


class GenderType(models.TextChoices):
    MALE = "male", _("Male")
    FEMALE = "female", _("Female")


class User(AbstractUser, TimeStampedModel):
    phone = PhoneNumberField(_("Phone number"), max_length=32, unique=True, null=True)
    email = models.EmailField(_("Email"), blank=True, null=True, unique=True)
    username = None
    first_name = None
    last_name = None
    full_name = models.CharField(_("Full name"), max_length=32, null=True, blank=True)
    gender = models.CharField(verbose_name=_("Gender"), max_length=10, choices=GenderType.choices, null=True)

    objects = UserManager()
    USERNAME_FIELD = "phone"
    REQUIRED_FIELDS = []  # type: ignore

    def __str__(self):
        if self.phone:
            return f"{self.phone}"
        if self.email:
            return f"{self.email}"

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")

