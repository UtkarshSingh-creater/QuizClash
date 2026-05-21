from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from .models import Question, Option


class CreateQuestionView(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request):

        question = Question.objects.create(
            room_id=request.data['room_id'],
            question_type=request.data['question_type'],
            text=request.data['text'],
            timer_seconds=request.data.get('timer_seconds', 10),
            points=request.data.get('points', 100),
            order=request.data.get('order', 1),
        )

        return Response(
            {
                'question_id': question.id,
                'message': 'Question created successfully'
            },
            status=status.HTTP_201_CREATED
        )


class CreateOptionView(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request):

        option = Option.objects.create(
            question_id=request.data['question_id'],
            text=request.data.get('text', ''),
            is_correct=request.data.get('is_correct', False)
        )

        return Response(
            {
                'option_id': option.id,
                'message': 'Option created successfully'
            },
            status=status.HTTP_201_CREATED
        )

class StartQuestionView(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request, question_id):

        question = Question.objects.get(id=question_id)

        question.status = 'ACTIVE'

        question.save()

        return Response({
            'message': 'Question started',
            'status': question.status
        })