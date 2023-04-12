from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from resumes.utils.constatns import RESUME_STATUS_CHOICES
from resumes.utils.validators import phone_regex_validator


class Specialty(models.Model):
    # For reviewers - in case we want to extend amount of specialties
    title = models.CharField(max_length=128)


class Resume(models.Model):
    status = models.CharField(max_length=128, choices=RESUME_STATUS_CHOICES)
    grade = models.PositiveIntegerField(null=True, validators=[MinValueValidator(1), MaxValueValidator(100)])
    specialty = models.ForeignKey(Specialty, on_delete=models.CASCADE, related_name="resumes")
    salary = models.PositiveIntegerField()
    education = models.CharField(max_length=512)
    experience = models.PositiveIntegerField(null=True)
    portfolio = models.URLField(null=True, blank=True)
    title = models.CharField(max_length=128)
    phone = models.CharField(max_length=17, validators=[phone_regex_validator])
    email = models.EmailField(max_length=128)
    author = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="resumes")
