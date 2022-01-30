import re
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():

    return {"username": "thisisrazakahn"}

@app.get("/posts")
async def get_posts():
    return {"name" : "this is your posts"}