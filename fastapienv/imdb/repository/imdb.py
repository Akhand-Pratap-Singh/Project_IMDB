from typing import List
from fastapi import APIRouter, Depends, status, HTTPException
from .. import schemas, database, models, hashing
from sqlalchemy.orm import Session
from ..test import a
import json

def get_movie_by_name(name:str, db:Session):
	movie = db.query(models.Imdb).filter(models.Imdb.name == name).first()
	try:
	    genre = List[json.loads(movie.genre)]
	except Exception as e:
		genre = movie.genre
	data = {
	        "popularity" : movie.popularity,
	        "director" : movie.director,
	        "genre" : genre,
	        "imdb_score" : movie.imdb_score,
	        "name" : movie.name,
	        "user_id" : 1
	        }
	if not movie:
		raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
							detail=f"Movie with the name {name} is not available")
	return data

def create(request:schemas.Blog, db:Session):
	new_value = models.Imdb(popularity=request.popularity,
								director=request.director,
								genre=request.genre,
								imdb_score=request.imdb_score,
								name=request.name,
								user_id=1)
	db.add(new_value)
	db.commit()
	db.refresh(new_value)
	return new_value

def create_json_dumb():
    pass