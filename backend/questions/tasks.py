from celery import shared_task
from .models import Question

@shared_task
def end_question(question_id):
    question=Question.objects.get(id=question_id)
    question.status='ENDED'
    question.save()