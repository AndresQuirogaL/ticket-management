from rest_framework import serializers

from api.models import Ticket


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ('images_quantity',)
