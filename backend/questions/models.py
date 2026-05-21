from django.db import models
from rooms.models import QuizRoom

class Question(models.Model):
    QUESTION_TYPES=(
        ('QUIZ','Quiz'),
        ('POLL','Poll'),
        ('SURVEY','Survey'),
        ('TRUE_FALSE','True False'),
    )
    STATUS_CHOICES=(
        ('WAITING','Waiting'),
        ('ACTIVE','Active'),
        ('PAUSED','Paused'),
        ('ENDED','Ended'),
    )
    room=models.ForeignKey(QuizRoom,on_delete=models.CASCADE)
    question_type=models.CharField(max_length=20,choices=QUESTION_TYPES)
    text=models.TextField()
    image=models.ImageField(upload_to='question_images/',null=True,blank=True)
    timer_seconds=models.IntegerField(default=10)
    points=models.IntegerField(default=100)
    negative_marks=models.IntegerField(default=0)
    order=models.IntegerField(default=1)
    status=models.CharField(max_length=20,choices=STATUS_CHOICES,default='WAITING')
    question_started_at=models.DateTimeField(null=True,blank=True)
    question_ends_at=models.DateTimeField(null=True,blank=True)
    is_paused=models.BooleanField(default=False)
    remaining_seconds=models.IntegerField(default=0)

class Option(models.Model):

    question=models.ForeignKey(Question,on_delete=models.CASCADE)
    text=models.CharField(max_length=255,blank=True)
    image=models.ImageField(upload_to='option_images/',null=True,blank=True)
    is_correct=models.BooleanField(default=False)