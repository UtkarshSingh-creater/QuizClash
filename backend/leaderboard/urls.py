from django.urls import path
from .views import LeaderboardView

urlpatterns=[
    path('<str:room_code>/',LeaderboardView.as_view()),
]