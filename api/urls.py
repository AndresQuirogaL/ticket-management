from rest_framework.authtoken import views
from django.conf.urls import url


urlpatterns = [
    url(
        r'^obtain-auth-token/',
        views.obtain_auth_token,
    ),
]
