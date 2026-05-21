from rest_framework.views import APIView
from rest_framework.response import Response
from participants.models import Participant
from questions.models import Question,Option
from .services import submit_answer

class SubmitAnswerView(APIView):
    def post(self,request):
        participant=Participant.objects.get(
            id=request.data['participant_id']
        )
        question=Question.objects.get(
            id=request.data['question_id']
        )
        option=Option.objects.get(
            id=request.data['option_id']
        )
        result=submit_answer(
            participant,
            question,
            option
        )

        return Response(result)