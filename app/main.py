from fastapi import FastAPI
from routers.users import router as user_router
from routers.posts import post_router


app = FastAPI()
app.include_router(router=user_router,)
app.include_router(router=post_router,)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app=app, host='0.0.0.0', port=8001, log_level='info',)
    
    