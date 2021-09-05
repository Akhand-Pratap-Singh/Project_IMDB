from typing import List
from fastapi import APIRouter, Depends, status
from .. import schemas, database, oauth2
from sqlalchemy.orm import Session
from ..repository import blog


get_db = database.get_db

router = APIRouter(
					prefix="/blog",
					tags=["BLOGS"]
					)


#all blogs at once
@router.get('/', response_model=List[schemas.ShowBlog])
def get_all_blogs(db:Session= Depends(get_db), current_user:schemas.User = Depends(oauth2.get_current_user)):
	return blog.get_all(db)

@router.post('/', status_code = status.HTTP_201_CREATED)
def create_new_blog(request:schemas.Blog, db:Session= Depends(get_db), current_user:schemas.User = Depends(oauth2.get_current_user)):
	return blog.create(request, db)

@router.get('/{id}', response_model=schemas.ShowBlog)
def get_blog_with_id(id:int, db: Session= Depends(get_db), current_user:schemas.User = Depends(oauth2.get_current_user)):
	return blog.get_blog(id, db)