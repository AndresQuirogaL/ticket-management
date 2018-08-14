from rest_framework import serializers

from api.models import Ticket
from api.models import TicketImage


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ('images_quantity',)


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = TicketImage
        fields = ('image',)
