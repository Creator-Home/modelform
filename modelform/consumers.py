# -- coding: utf-8 --
"""
Consumers are used for making websocket connections
"""
import json
import logging
from channels.generic.websocket import AsyncJsonWebsocketConsumer

LOG = logging.getLogger(__name__)


class TestConsumer(AsyncJsonWebsocketConsumer):
    """
    creates websocket connections
    """

    async def connect(self):
        """
        handles incoming connections to websocket
        """
        self.room_name = "testing"
        self.room_group_name = 'room_%s' % self.room_name

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        """
        handles disconnection from websocket
        """
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        """
        Receive message from WebSocket.
        Get the event and send the appropriate event
        :params text_data : receives data in format
                            {"type":"send_message", "message":<YOUR MESSAGE>, "event":"UPDATE"}
        """
        response = json.loads(text_data)
        event = response.get("event", None)
        message = response.get("message", None)
        if event == 'UPDATE':
            # Send message to room group
            await self.channel_layer.group_send(self.room_group_name, {
                'type': 'send_message',
                'message': message,
                "event": "UPDATE"
            })

    async def send_message(self, res):
        """
        Receive message from room group
        """
        # Send message to WebSocket
        message = res.get("message", None)
        await self.send(text_data=json.dumps({
            "payload": message
        }))
