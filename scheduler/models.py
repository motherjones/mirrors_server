from django.db import models


class Reservation(models.Model):
    slug = models.CharField(max_length=255)
    datetime = models.DateTimeField()
    # component_revision = model.IntegerField()
