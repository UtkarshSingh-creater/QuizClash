from django.db import models

from accounts.models import User


class QuizRoom(models.Model):

    STATUS_CHOICES = (
        ('WAITING', 'Waiting'),
        ('ACTIVE', 'Active'),
        ('ENDED', 'Ended'),
    )

    host = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    room_code = models.CharField(
        max_length=8,
        unique=True
    )

    title = models.CharField(max_length=255)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='WAITING'
    )

    current_question_index = models.IntegerField(default=0)