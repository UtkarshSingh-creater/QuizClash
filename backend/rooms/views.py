import random
import string

from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from .models import QuizRoom


class CreateRoomView(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request):

        title = request.data.get('title')

        if not title:

            return Response(
                {'error': 'Title is required'},
                status=status.HTTP_400_BAD_REQUEST
            )

        room_code = ''.join(
            random.choices(
                string.ascii_uppercase + string.digits,
                k=6
            )
        )

        room = QuizRoom.objects.create(
            host=request.user,
            title=title,
            room_code=room_code
        )

        return Response(
            {
                'room_code': room.room_code
            },
            status=status.HTTP_201_CREATED
        )