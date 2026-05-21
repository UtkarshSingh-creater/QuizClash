from django.db import models
from participants.models import Participant
from questions.models import Question,Option

class Answer(models.Model):
    participant=models.ForeignKey(Participant,on_delete=models.CASCADE)
    question=models.ForeignKey(Question,on_delete=models.CASCADE)
    selected_option=models.ForeignKey(Option,on_delete=models.CASCADE)
    response_time=models.FloatField()
    points_earned=models.IntegerField(default=0)
    answered_at=models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together=('participant','question')