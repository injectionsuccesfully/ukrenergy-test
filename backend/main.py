from fastapi import FastAPI
from routers import files
from services.app.appinitializer import AppInitializerService

AppInitializerService().initialize_db()

app = FastAPI()
app.include_router(files.router)

