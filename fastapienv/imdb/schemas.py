from typing import Optional
from pydantic import BaseModel

class Blog(BaseModel):
	title: str
	body: str

class Imdb(BaseModel):
	popularity: float
	director: str
	imdb_score: float
	name: str
	genre: str
	user_id:int

class ShowImdb(Imdb):
	class Config():
		orm_mode = True

class ShowBlog(Blog):
	class Config():
		orm_mode = True

class User(BaseModel):
	name: str
	email: str
	password: str
	admin_rights: bool

class ShowUser(BaseModel):
	name: str
	email: str
	admin_rights: bool
	class Config():
		orm_mode = True

class Login(BaseModel):
	username: str
	password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[str] = None