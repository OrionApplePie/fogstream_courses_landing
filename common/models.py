from django.db import models


class Feedback(models.Model):
    email = models.CharField(max_length=32, null=False, blank=False)
    name = models.CharField(max_length=32, null=True, blank=True)
    subject = models.CharField(max_length=24, null=True, blank=True)
    message = models.CharField(max_length=255, null=False, blank=False)

    def __str__(self):
        return self.email
