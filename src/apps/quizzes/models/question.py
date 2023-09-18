from django.db import models
from django.utils.translation import gettext_lazy as _

from src.apps.quizzes.models.quiz import Quizzes
from src.apps.quizzes.models.updated import Updated


class DifficultChoice(models.TextChoices):
    FUNDAMENTAL = ('FUNDAMENTAL', _('Fundamental'))
    BEGINNER = ('BEGINNER', _('Beginner'))
    INTERMEDIATE = ('INTERMEDIATE', _('Intermediate'))
    ADVANCED = ('ADVANCED', _('Advanced'))
    EXPERT = ('EXPERT', _('Expert'))


class Question(Updated):
    quiz = models.ForeignKey(
        Quizzes, related_name='questions', on_delete=models.CASCADE)

    title = models.CharField(max_length=255, verbose_name=_("Title"))
    difficulty = models.CharField(
        choices=DifficultChoice.choices, max_length=15, default='FUNDAMENTAL', verbose_name=_("Difficulty"))
    date_created = models.DateTimeField(
        auto_now_add=True, verbose_name=_("Date Created"))
    is_active = models.BooleanField(
        default=False, verbose_name=_("Active Status"))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Question")
        verbose_name_plural = _("Questions")
        ordering = ['id']
