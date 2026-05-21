import json

from channels.generic.websocket import AsyncWebsocketConsumer


class QuizConsumer(AsyncWebsocketConsumer):

    async def connect(self):

        self.room_code=self.scope['url_route']['kwargs']['room_code']
        self.room_group_name=f'quiz_{self.room_code}'

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

        await self.send(
            text_data=json.dumps({
                'message':'WebSocket connected'
            })
        )


    async def disconnect(self, close_code):

        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )


    async def receive(self, text_data):

        data=json.loads(text_data)

        message=data['message']

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type':'quiz_message',
                'message': message
            }
        )


    async def quiz_message(self, event):

        message=event['message']

        await self.send(
            text_data=json.dumps({
                'message': message
            })
        )