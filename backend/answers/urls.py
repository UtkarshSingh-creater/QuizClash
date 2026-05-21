from django.urls import path
from .views import SubmitAnswerView

urlpatterns=[
    path('submit/',SubmitAnswerView.as_view()),
]