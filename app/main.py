from fastapi import FastAPI
from routers.users import router as user_router
from routers.posts import post_router

# Uncomment this file comments, when you are ready to pull redis image from hub.docker.io 
# from utils.cache import start_redis
# from contextlib import asynccontextmanager


# @asynccontextmanager
# async def app_lifespan(app: FastAPI):
#     await start_redis()
# 
# app = FastAPI(lifespan=app_lifespan)

app = FastAPI()

app.include_router(router=user_router,)
app.include_router(router=post_router,)

    
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app=app, host='0.0.0.0', port=8001,)
    