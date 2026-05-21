import random
import uuid

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rooms.models import QuizRoom

from .models import Participant


class JoinRoomView(APIView):

    def post(self, request):

        room_code = request.data.get('room_code')

        if not room_code:

            return Response(
                {'error': 'Room code is required'},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:

            room = QuizRoom.objects.get(room_code=room_code)

        except QuizRoom.DoesNotExist:

            return Response(
                {'error': 'Room not found'},
                status=status.HTTP_404_NOT_FOUND
            )

        nickname = request.data.get('nickname')

        if not nickname:

            nickname = f'Player{random.randint(1000,9999)}'

        participant = Participant.objects.create(
            room=room,
            nickname=nickname,
            session_id=uuid.uuid4(),
            is_guest=True
        )

        return Response(
            {
                'participant_id': participant.id,
                'session_id': str(participant.session_id),
                'nickname': participant.nickname,
            },
            status=status.HTTP_201_CREATED
        )