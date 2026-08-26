from fastapi import FastAPI

from web.routes import router

app = FastAPI(title="Windchill REST Studio")

app.include_router(router)
