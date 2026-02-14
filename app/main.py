from fastapi import FastAPI
from .database import Base, engine
from .routers import generate, specs, health
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()




app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


Base.metadata.create_all(bind=engine)

app.include_router(generate.router, prefix="/generate")
app.include_router(specs.router, prefix="/specs")
app.include_router(health.router, prefix="/health")
