from rest_framework.authtoken import views
from django.conf.urls import url

from api.views import TicketView


urlpatterns = [
    url(
        r'^obtain-auth-token/',
        views.obtain_auth_token,
    ),

    url(
        r'^tickets/$',
        TicketView.as_view(),
    ),
]
