from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
# import uvicorn

app = FastAPI()

@app.get('/') #for localhost
def index():
	return {'data':'bog list'}

@app.get('/blog/{id}')
def show(id:int):
	return {'data':id}

@app.get('/blog/{id}/comments')
def comments(id):
	#fetch comments of blog with id = id
	return {'data':{'1', '2'}}

@app.get('/queryparameter')
def show(limit=10, status:bool=True, sort: Optional[str] = None):
	#limit is the parameter provided in url
	#http://localhost:8000/queryparameter?limit=10
	return {'data': f'{limit} given in limit parameter second parameter is {status}'}


class Blog(BaseModel):
	title: str
	body: str
	published: Optional[bool]

@app.post('/blog')
def create_blog(blog: Blog):
	#blog: Blog == request: Blog
	# import pdb;pdb.set_trace()
	return {'data': f"Blog is created with title as {blog.title}"}


# # for port change
# if __name__ == "__main__":
# 	uvicorn.run(app, host="127.0.0.1", port=9000)