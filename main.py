from fastapi import FastAPI

from router import user, login

app = FastAPI()

app.include_router(login.router, prefix="/api/v1", tags=["login"])
app.include_router(user.router, prefix="/api/v1/users", tags=["users"])