# Template file to start a new project based on FastAPI.

from fastapi import FastAPI, Response


app = FastAPI()


@app.get('/demo/{param}')
async def home(param: int|None = 33):
    return {'param': param + 1000}


@app.get('/robots.txt')
async def robotstxt():
    return Response(content='Disallow: /', media_type='text/plain')
