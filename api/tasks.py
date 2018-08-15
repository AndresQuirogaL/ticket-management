from huey.contrib.djhuey import db_task

from api.models import COMPLETED_TICKET
from api.models import Ticket


@db_task()
def upload_image_task(serializer, ticket_id):
    """
    Second level task to upload ticket images.
    """
    ticket = Ticket.objects.get(id=ticket_id)

    serializer.save(ticket=ticket)

    if ticket.ticketimage_set.count() >= ticket.images_quantity:
        ticket.status = COMPLETED_TICKET
        ticket.save()
