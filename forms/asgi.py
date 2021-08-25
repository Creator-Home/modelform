"""
ASGI config for forms project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'forms.settings')
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from channels.security.websocket import AllowedHostsOriginValidator, OriginValidator

import modelform.routing

"""
Handles two types of requests i.e. http requests and websocket request
AllowedHostsOriginValidator : validation for ALLOWED_HOSTS
"""
#http://
#ws://
application = ProtocolTypeRouter({
  "http": get_asgi_application(),
  "websocket": AllowedHostsOriginValidator(
        URLRouter(
          modelform.routing.websocket_urlpatterns
        )
  ),
})
