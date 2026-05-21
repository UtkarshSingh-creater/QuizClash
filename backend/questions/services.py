from django.utils import timezone
from datetime import timedelta

def pause_question(question):
    question.is_paused=True

    remaining=(
        question.question_ends_at-timezone.now()
    ).total_seconds()

    question.remaining_seconds=int(remianing)
    question.save()

def resume_question(question):
    question.is_paused=False
    question.question_ends_at=(
        timezone.now()+timedelta(
            seconds=question.remaining_seconds
        )
    )
    question.save()

def extend_timer(question,extra_seconds):
    question.question_ends_at+=timedelta(
        seconds=extra_seconds
    )
    question.save()