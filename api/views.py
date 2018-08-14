from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from api.serializers import TicketSerializer
from api.serializers import ImageSerializer
from api.models import Ticket
from api.models import PENDING_TICKET
from api.models import COMPLETED_TICKET


class TicketView(APIView):
    def post(self, request, format=None):
        serializer = TicketSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(created_by=request.user)

            return Response(
                serializer.data,
                status=status.HTTP_200_OK,
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )


class ImageView(APIView):
    def post(self, request, ticket_id, format=None):
        ticket = get_object_or_404(
            Ticket,
            id=ticket_id,
            status=PENDING_TICKET,
            created_by=request.user,
        )

        serializer = ImageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(ticket=ticket)

            if ticket.ticketimage_set.count() == ticket.images_quantity:
                ticket.status = COMPLETED_TICKET
                ticket.save()

            return Response(
                serializer.data,
                status=status.HTTP_200_OK,
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )
