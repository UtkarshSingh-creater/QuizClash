from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

channel_layer=get_channel_layer()

def broadcast_question(room_code,data):
    async_to_sync(channel_layer.group_send)(
        f'quiz_{room_code}',
        {
            'type':'send_question',
            'data':data,
        }
    )

def broadcast_leaderboard(room_code,data):
    async_to_sync(channel_layer.group_send)(
        f'quiz_{room_code}',
        {
            'type':'leaderboard_update',
            'data':data,
        }
    )