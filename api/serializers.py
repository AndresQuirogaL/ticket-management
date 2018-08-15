from rest_framework import serializers

from api.models import Ticket
from api.models import TicketImage


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ('images_quantity',)


class GetTicketSerializer(serializers.ModelSerializer):
    images_count = serializers.CharField(
        source='get_images_count'
    )

    current_status = serializers.CharField(
        source='get_status_display'
    )

    images_list = serializers.CharField(
        source='get_images_list'
    )

    class Meta:
        model = Ticket
        fields = (
            'id',
            'created_at',
            'images_quantity',
            'images_count',
            'current_status',
            'images_list',
        )

        read_only_fields = (
            'images_count',
            'current_status',
            'images_list',
        )


class ImageSerializer(serializers.ModelSerializer):
    ticket_id = serializers.CharField(
        source='get_ticket_id',
        required=False,
    )

    ticket_status = serializers.CharField(
        source='get_ticket_status',
        required=False,
    )

    images_count = serializers.CharField(
        source='get_images_count',
        required=False,
    )

    class Meta:
        model = TicketImage
        fields = (
            'image',
            'ticket_id',
            'images_count',
            'ticket_status',
        )

        read_only_fields = (
            'ticket_id',
            'images_count',
            'ticket_status'
        )
