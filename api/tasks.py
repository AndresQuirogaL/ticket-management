from huey.contrib.djhuey import db_task

from api.models import COMPLETED_TICKET


# @db_task()
def upload_image_task(serializer, ticket):
    """
    Second level task to upload ticket images.
    """
    serializer.save(ticket=ticket)

    if ticket.ticketimage_set.count() >= ticket.images_quantity:
        ticket.status = COMPLETED_TICKET
        ticket.save()
