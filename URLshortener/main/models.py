from django.db import models
from django.utils import timezone


# Create your models here.
class LinkMapping(models.Model):
    original_url = models.CharField(max_length=256)
    hash = models.CharField(max_length=10, unique=True, db_index=True)
    creation_date = models.DateTimeField('creation date')
    deletion_date = models.DateTimeField(default=timezone.now,
                                         blank=True, )


