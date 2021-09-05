from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey
from .database import Base
from sqlalchemy.orm import relationship


class Blog(Base):
	__tablename__ = 'blogs'

	id = Column(Integer, primary_key=True, index = True)
	title = Column(String)
	body = Column(String)

class Imdb(Base):
	__tablename__ = 'imdb'

	id = Column(Integer, primary_key=True, index = True)
	popularity = Column(Float)
	director = Column(String)
	imdb_score = Column(Float)
	name = Column(String)
	genre = Column(String)
	user_id = Column(Integer, ForeignKey("users.id"))

	user = relationship("User", back_populates = "imdb")

class User(Base):
	__tablename__ = 'users'

	id = Column(Integer, primary_key=True, index = True)
	name = Column(String)
	email = Column(String)
	password = Column(String)
	admin_rights = Column(Boolean, default=False)


	imdb = relationship("Imdb", back_populates = "user")

