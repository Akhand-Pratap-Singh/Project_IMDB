from fastapi import APIRouter, Depends
from .. import schemas, database
from sqlalchemy.orm import Session
from ..repository import user

get_db = database.get_db

router = APIRouter(
					prefix="/user",
					tags=["USERS"]
					)

@router.post('/', response_model=schemas.ShowUser)
def create_user(request:schemas.User, db: Session= Depends(get_db)):
	
	return user.create(request, db)