"""
ASGI config for chatWS project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from django.core.asgi import get_asgi_application
# AllowedHostsOriginValidator - страшно удобная штукА!

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'prjchat.settings')
django_asgi_app = get_asgi_application()


import appchat.routing


application = ProtocolTypeRouter(
    {
        "http": django_asgi_app,
        "websocket": AllowedHostsOriginValidator(
            AuthMiddlewareStack(URLRouter(appchat.routing.websocket_urlpatterns))
        ),
    }
)
