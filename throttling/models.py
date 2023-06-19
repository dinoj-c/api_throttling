from django.db import models


class Throttle(models.Model):
    referrer = models.CharField(max_length=255)
    request_time = models.DateTimeField(auto_now_add=True)
