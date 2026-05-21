from django.urls import path
from .views import JoinRoomView

urlpatterns=[
    path('join/',JoinRoomView.as_view()),
]