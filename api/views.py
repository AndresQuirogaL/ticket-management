from datetime import datetime
from rest_framework import generics

from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.core.files.storage import FileSystemStorage

from api.serializers import TicketSerializer
from api.serializers import GetTicketSerializer
from api.serializers import ImageSerializer
from api.models import Ticket
from api.tasks import upload_image_from_disk_task
from api.models import PENDING_TICKET
from api.models import COMPLETED_TICKET


def get_verified_date(date):
    initial_date_query = None
    try:
        initial_date_query = datetime.strptime(
            date,
            '%Y-%m-%d',
        )

    except ValueError:
        # If the date is not in the correct format,
        # the filter will not be called.
        pass

    return initial_date_query


class TicketView(generics.ListCreateAPIView):
    model = Ticket

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return TicketSerializer
        return GetTicketSerializer

    def get_queryset(self):
        queryset = Ticket.objects.filter(
            created_by=self.request.user,
        )

        # Filter by status.
        status = self.request.GET.get('status', '')
        status_query = None

        if status == 'completado':
            status_query = COMPLETED_TICKET

        elif status == 'pendiente':
            status_query = PENDING_TICKET

        if status_query:
            queryset = queryset.filter(status=status_query)

        # # Filter by date range.

        # Initial Date.
        initial_date = self.request.GET.get('initial_date', '')
        initial_date_query = None

        if initial_date:
            initial_date_query = get_verified_date(initial_date)

        if initial_date_query:
            queryset = queryset.filter(created_at__gte=initial_date_query)

        # End Date.
        end_date = self.request.GET.get('end_date', '')
        end_date_query = None

        if end_date:
            end_date_query = get_verified_date(end_date)

        if end_date_query:
            queryset = queryset.filter(created_at__lte=end_date_query)

        return queryset

    def create(self, request, *args, **kwargs):
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


class TicketDetailView(generics.RetrieveAPIView):
    queryset = Ticket.objects.all()
    serializer_class = GetTicketSerializer

    def get_object(self):
        queryset = self.get_queryset()
        ticket = get_object_or_404(
            queryset,
            id=self.kwargs['ticket_id'],
            created_by=self.request.user
        )

        return ticket


class ImageView(generics.CreateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = ImageSerializer

    def get_object(self):
        queryset = self.get_queryset()

        return get_object_or_404(
            queryset,
            id=self.kwargs['ticket_id'],
            status=PENDING_TICKET,
            created_by=self.request.user
        )

    def create(self, request, *args, **kwargs):
        serializer = ImageSerializer(data=request.data)
        if serializer.is_valid():
            ticket = self.get_object()

            folder = 'app/static/uploads/'
            image = request.FILES['image']

            fs = FileSystemStorage(location=folder)
            file_name = fs.save(image.name, image)
            file_url = fs.url(file_name)

            upload_image_from_disk_task(
                ticket_id=ticket.id,
                file_name=file_name,
                file_url=file_url,
            )

            return Response(
                status=status.HTTP_200_OK,
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )
