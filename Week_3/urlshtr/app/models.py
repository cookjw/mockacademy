from django.db import models

class ShortenedURL(models.Model):
    original_url = models.URLField()
    shrtd = models.CharField(max_length=16)
    

class ApplicationState(models.Model):
    next_id = models.IntegerField(default=1)
    

