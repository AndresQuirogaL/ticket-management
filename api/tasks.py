import os
from django.core.files import File
from huey.contrib.djhuey import db_task
import urllib.request

from api.models import COMPLETED_TICKET
from api.models import Ticket
from api.models import TicketImage


# @db_task()
# def upload_image_task(serializer, ticket_id):
#     """
#     Second level task to upload ticket images.
#     """
#     ticket = Ticket.objects.get(id=ticket_id)

#     serializer.save(ticket=ticket)

#     if ticket.ticketimage_set.count() >= ticket.images_quantity:
#         ticket.status = COMPLETED_TICKET
#         ticket.save()


@db_task()
def upload_image_from_disk_task(ticket_id, file_name, file_url):
    ticket = Ticket.objects.get(id=ticket_id)

    url = "http://localhost:8000/static/uploads/{}".format(
        file_url
    )

    result = urllib.request.urlretrieve(url)

    ticket_image = TicketImage.objects.create(
        ticket=ticket,
    )

    ticket_image.image.save(
        os.path.basename(url),
        File(open(result[0], 'rb'))
    )

    if ticket.ticketimage_set.count() >= ticket.images_quantity:
        ticket.status = COMPLETED_TICKET
        ticket.save()

    os.remove('app/static/uploads/{}'.format(file_name))
