from django.db import models
from django.core.exceptions import ValidationError
import datetime


def validate_future_date(value):
    if value < datetime.datetime.utcnow():
        raise ValidationError('Datetime is in the past.')

class Reservation(models.Model):
    """
        A Reservation is a time when a component should be published.
    """
    slug = models.CharField(max_length=255)
    datetime = models.DateTimeField(validators=[validate_future_date])
    # component_revision = model.IntegerField()
