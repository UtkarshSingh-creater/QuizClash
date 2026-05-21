from rest_framework.views import APIView
from rest_framework.response import Response
from .services import get_top_players

class LeaderboardView(APIView):
    def get(self,request,room_code):
        leaderboard=get_top_players(room_code)

        return Response({
            'leaderboard':leaderboard
        })