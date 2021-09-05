from fastapi import APIRouter, Depends, status, HTTPException
from .. import schemas, database, models, hashing
from sqlalchemy.orm import Session
from ..test import a
import json
from ..hashing import Hash


get_db= database.get_db


def create(request, db:Session):
	new_user = models.User(name=request.name,
						   email=request.email, 
						   password=hashing.Hash.bcrypt(request.password), 
						   admin_rights=request.admin_rights)
	db.add(new_user)
	db.commit()
	db.refresh(new_user)
	return new_user

def get_user_rights(request, db:Session, current_user:schemas.User):
	# import pdb;pdb.set_trace()
	user = db.query(models.User).filter(models.User.id == request.user_id).first()
	return user.admin_rights