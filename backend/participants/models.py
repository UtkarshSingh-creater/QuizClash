import uuid
from django.db import models
from rooms.models import QuizRoom
from accounts.models import User

class Participant(models.Model):
    room=models.ForeignKey(QuizRoom,on_delete=models.CASCADE)
    user=models.ForeignKey(User,null=True,blank=True,on_delete=models.SET_NULL)
    nickname=models.CharField(max_length=50)
    session_id=models.UUIDField(default=uuid.uuid4,editable=False)
    score=models.IntegerField(default=0)
    streak=models.IntegerField(default=0)
    rank=models.IntegerField(default=0)
    is_guest=models.BooleanField(default=True)
    joined_at=models.DateTimeField(auto_now_add=True)