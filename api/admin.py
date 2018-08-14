from django.contrib import admin
from django.contrib.auth.models import Group

from api.models import Ticket
from api.models import TicketImage


admin.site.unregister(Group)


class TicketImageInline(admin.TabularInline):
    model = TicketImage
    extra = 1


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'created_by',
        'created_at',
        'status',
    )

    list_filter = (
        'created_by',
        'created_at',
        'status',
    )

    inlines = [
        TicketImageInline,
    ]
