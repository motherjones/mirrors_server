from scheduler.models import Reservation
from scheduler.serializers import ReservationSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import pdb


class ReservationList(APIView):
    """
    ReservationList is for nonspecific Reservation requests, like
    obtaining all Reservations or creating a new Reservation.
    """
    def post(self, request, format=None):
        serializer = ReservationSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ReservationDetail(APIView):
    """
    ReservationDetail is for retrieving or modifying a specific
    Reservation.
    """
    def get_object(self, pk):
        try:
            return Reservation.objects.get(pk=pk)
        except Reservation.DoesNotExist:
            raise Http404

    def patch(self, request, pk, format=None):
        reservation = self.get_object(pk)
        serializer = ReservationSerializer(reservation, data=request.DATA)
        pdb.set_trace()
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
