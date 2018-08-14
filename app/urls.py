from django.conf.urls import include
from django.conf.urls import url
from django.contrib import admin

admin.site.site_title = 'Gestión de tickets'
admin.site.site_header = 'Gestión de tickets - Administrador'

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(
        r'^api/',
        include(
            (
                'api.urls',
                'api',
            ),
            namespace='api'
        )
    ),
]
