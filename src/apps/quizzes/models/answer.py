from django.db import models
from django.utils.translation import gettext_lazy as _

from src.apps.quizzes.models.question import Question
from src.apps.quizzes.models.updated import Updated


class Answer(Updated):
    question = models.ForeignKey(
        Question, related_name='answers', on_delete=models.CASCADE)

    answer_text = models.CharField(
        max_length=255, verbose_name=_("Answer Text"))
    is_right = models.BooleanField(default=False)

    def __str__(self):
        return self.answer_text

    class Meta:
        verbose_name = _("Answer")
        verbose_name_plural = _("Answers")
        ordering = ['id']
