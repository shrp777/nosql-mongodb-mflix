from .routers import movies
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from fastapi.responses import PlainTextResponse, JSONResponse
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import ValidationError


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    # autorise les requêtes HTTP en provenance de toutes les origines
    allow_origins=["*"],
    # autorise les headers HTTP Authorization
    allow_credentials=True,
    # autorise tous les verbes HTTP
    allow_methods=["*"],
    # autorise tous les headers HTTP
    allow_headers=["*"],
)


app.include_router(movies.router)


@app.get("/")
def read_root():
    """
    Racine de l'API
    """
    return {"message": "movies API"}
