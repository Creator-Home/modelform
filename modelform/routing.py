# -- coding: utf-8 --
"""
routers for ASGI connection in django
"""

from django.conf.urls import url

from modelform.consumers import TestConsumer

websocket_urlpatterns = [
    url(r'^ws/testcounter/$', TestConsumer.as_asgi()),
]
