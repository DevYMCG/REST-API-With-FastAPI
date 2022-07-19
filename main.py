from fastapi import FastAPI

from router.user import router as user_router
from router.login  import router as login_router

app = FastAPI()

app.include_router(login_router, tags=["login"])
app.include_router(user_router, prefix="/users", tags=["users"])