from fastapi import FastAPI
from . import models, database
from .routes import url

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(

    title="URL Shortener API",
    description="An API to shorten URLs and redirect them",
    version="1.0.0"
)


app.include_router(url.router)
