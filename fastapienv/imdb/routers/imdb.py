from typing import List
from fastapi import APIRouter, Depends, status, HTTPException
from .. import schemas, database, models, hashing, oauth2
from sqlalchemy.orm import Session
from ..test import a
from ..repository import imdb, user
import json
get_db= database.get_db

router = APIRouter(
					prefix="/imdb",
					tags=["IMDB"]
					)

@router.get('/', response_model=schemas.ShowImdb)
def get_movie_by_name(
					name:str, 
					db:Session= Depends(get_db), 
					current_user:schemas.User = Depends(oauth2.get_current_user)):
	return imdb.get_movie_by_name(name, db)

@router.post('/', status_code = status.HTTP_201_CREATED)
def create_imdb(request:schemas.Imdb, db:Session= Depends(get_db), 
	current_user:schemas.User = Depends(oauth2.get_current_user)):
	if not user.get_user_rights(request, db, current_user):
		raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
							detail=f"Sorry you are not autherized to perform create action")

	return imdb.create(request, db)


# # -----------------------------------------------------------------------------
# # dump json data
# @router.post('/blog', status_code = status.HTTP_201_CREATED)
# def create(request:schemas.Imdb, db:Session= Depends(get_db)):
# 	value_list = a
# 	for value in value_list:
# 		popularity = value.get("99popularity", 0.0)
# 		director = value.get("director", 'Akhand')
# 		genre_list = value.get("genre", 'Nothing')
# 		genre = json.dumps(genre_list)
# 		imdb_score = value.get("imdb_score", 0.0)
# 		name = value.get("name", 'Akhand Pratap Singh')

# 		new_value = models.Imdb(popularity=popularity,
# 								director=director,
# 								genre=genre,
# 								imdb_score=imdb_score,
# 								name=name,
# 								user_id=1)
# 		db.add(new_value)
# 		db.commit()
# 		db.refresh(new_value)
# 	return new_value

# # ---------------------------------------------------------------------------