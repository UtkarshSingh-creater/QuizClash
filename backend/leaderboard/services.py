import redis

r=redis.Redis(
    host='localhost',
    port=6379,
    decode_responses=True
)

def update_leaderboard(room_code,participant_id,score):
    r.zadd(
        f'leaderboard:{room_code}',
        {participant_id:score}
    )

def get_top_players(room_code):
    return r.zrevrange(
        f'leaderboard:{room_code}',
        0,
        9,
        withscores=True
    )