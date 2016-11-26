from django.db import models


class Cool(models.Model):
    name = models.CharField(max_length=22, null=False, blank=False)