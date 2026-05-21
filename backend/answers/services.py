from .models import Answer
from leaderboard.services import update_leaderboard


def submit_answer(participant, question, option):

    if question.status != 'ACTIVE':

        return {
            'message': 'Question inactive'
        }

    correct = option.is_correct

    points_earned = 0

    if correct:

        points_earned = question.points

        participant.score += points_earned

        participant.save()
        update_leaderboard(
            participant.room.room_code,
            participant.nickname,
            participant.score
        )

    answer = Answer.objects.create(
        participant=participant,
        question=question,
        selected_option=option,
        response_time=1.0,
        points_earned=points_earned
    )

    return {
        'correct': correct,
        'points_earned': points_earned
    }