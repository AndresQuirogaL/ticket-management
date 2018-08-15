from huey.contrib.djhuey import db_task

from api.models import COMPLETED_TICKET
from api.models import TicketImage


@db_task(retries=0, retry_delay=60)
def upload_image_task(ticket, image):
    """
    Second level task to upload ticket images.
    """
    # TicketImage.objects.create(
    #     ticket=ticket,
    #     image=image,
    # )

    if ticket.ticketimage_set.count() >= ticket.images_quantity:
        ticket.status = COMPLETED_TICKET
        ticket.save()
