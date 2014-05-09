from django.db import models


class Reservation(models.Model):
    """
        A Reservation is a time when a component should be published.
    """
    slug = models.CharField(max_length=255)
    datetime = models.DateTimeField()
    # component_revision = model.IntegerField()
