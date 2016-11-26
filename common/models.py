from django.db import models


class Feedback(models.Model):
    name = models.CharField(max_length=32, blank=False, null=False)
    email = models.EmailField(null=False, blank=False)
    subject = models.CharField(max_length=32, blank=True, null=True)
    message = models.CharField(max_length=255, null=False, blank=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    answer = models.TextField(default='')
    is_reply = models.BooleanField(default=False, blank=False, null=False)

    def __str__(self):
        return self.name


'''test'''