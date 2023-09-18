from django.db import models
from django.utils.translation import gettext_lazy as _

from src.apps.quizzes.models.category import Category


class Quizzes(models.Model):
    title = models.CharField(max_length=255, default=_(
        "New Quiz"), verbose_name=_("Quiz Title"))
    category = models.ForeignKey(
        Category, related_name='quizzes', default=1, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("Quiz")
        verbose_name_plural = _("Quizzes")
        ordering = ['id']

    def __str__(self):
        return self.title
