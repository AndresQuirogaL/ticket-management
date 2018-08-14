from rest_framework.authtoken import views
from django.conf.urls import url

from api.views import TicketView
from api.views import ImageView


urlpatterns = [
    url(
        r'^obtain-auth-token/',
        views.obtain_auth_token,
    ),

    url(
        r'^tickets/$',
        TicketView.as_view(),
    ),

    url(
        r'^imagen/(?P<ticket_id>\d+)/$',
        ImageView.as_view(),
    ),
]
