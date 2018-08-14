from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from api.serializers import TicketSerializer


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
