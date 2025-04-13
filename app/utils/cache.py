"""
This file is commented due to Internet issues, I couldn't able to pull redis image from the docker hub.
"""
# import redis.asyncio as redis
# from fastapi_cache import FastAPICache
# from fastapi_cache.backends.redis import RedisBackend


# async def start_redis():
#     redis_client = redis.from_url(
#         "redis://redis:6379",
#         encoding='utf-8',
#         decode_responses=True,
#     )
#     FastAPICache.init(RedisBackend(redis_client))