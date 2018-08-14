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

    class Meta:
        model = Ticket
        fields = (
            'images_quantity',
            'images_count',
            'current_status',
        )

        read_only_fields = (
            'images_count',
            'current_status',
        )


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = TicketImage
        fields = ('image',)
