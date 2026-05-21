from answers.models import Answer

def calculate_average_response(question):
    answers=Answer.objects.filter(question=question)

    if not answers.exists():
        return 0

    total=sum(a.response_time for a in answers)

    return total/answers.count()