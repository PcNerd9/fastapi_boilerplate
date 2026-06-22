from redis.asyncio import Redis

from core.config import settings

redis_client: Redis | None = None

async def init_redis():
    global redis_client
    
    redis_client = Redis.from_url(
        settings.REDIS_URL,
        decode_response=True
    )
    
async def close_redis():
    if redis_client:
        await redis_client.close()
        
        
def get_redis():
    if not redis_client:
        raise RuntimeError("Redis is not Initialized")
    return redis_client