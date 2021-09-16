#sync_to_asyn
#channel layer
#send message
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer

def post_save_college_record(**kwargs):
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)('room_testing', {
        'type': 'send_message',
        'message': "New class addition ended",
        'event': 'MOVE'})
    print("New class addition ended")

def pre_save_college_record(**kwargs):
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)('room_testing', {
        'type': 'send_message',
        'message': "New class addition started",
        'event': 'MOVE'}
                                            )
    print("New class addition started")