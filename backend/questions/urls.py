from django.urls import path
from .views import (
    CreateQuestionView,
    CreateOptionView,
    StartQuestionView,
)

urlpatterns=[
    path('create/',CreateQuestionView.as_view()),
    path('options/create/', CreateOptionView.as_view()),
    path('<int:question_id>/start/',StartQuestionView.as_view()),
]