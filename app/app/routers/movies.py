from fastapi import APIRouter, HTTPException, Depends

from typing import List

from ..models.movie import Movie, MovieCreateDTO, MovieModel

from ..db import db

from bson import ObjectId

router = APIRouter()


@router.on_event("startup")
async def startup_db():
    await db.connect()


@router.on_event("shutdown")
async def shutdown_db():
    await db.close()


@router.get("/movies", response_model=List[MovieModel], status_code=200)
async def get_items():
    """
    Récupère la liste des items
    """
    movies_cursor = db.database["movies"].find()
    movies = []
    async for movie in movies_cursor:
        movie["title"] = str(movie["title"])
        movies.append(movie)
    return movies
