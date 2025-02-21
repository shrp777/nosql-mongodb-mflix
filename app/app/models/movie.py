import os

from pydantic import BaseModel
from typing import Optional


class MovieModel(BaseModel):
    id: Optional[str] = None
    title: str


class MovieCreateDTO(MovieModel):
    """
    Movie sans id (utile pour la création)
    """
    pass


class Movie(MovieModel):
    """
    Movie avec id
    """
    id: int

    class Config:
        from_attributes = True
