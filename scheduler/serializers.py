from rest_framework import serializers
from scheduler.models import Reservation

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = ('id', 'slug', 'datetime')
