from django.db import models
from django.utils.translation import gettext_lazy as _


class Updated(models.Model):
    date_updated = models.DateTimeField(
        verbose_name=_("Last Updated"), auto_now=True)

    class Meta:
        abstract = True