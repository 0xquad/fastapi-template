# Template file to start a new project based on FastAPI.
# TODO: Remove this comment

import os, os.path
import yaml
import json
import aiofiles
import aiohttp
import logging
from fastapi import FastAPI, Response, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel


def load_config():
    conf_file = os.environ.get('CONFIG', 'config.yaml')
    with open(conf_file, 'r') as f:
        config = yaml.safe_load(f.read())

    return config['config']


app = FastAPI()
app.config = load_config()

logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


@app.get('/demo/get/{param}')   # handles also /demo/get?param
async def home(param: int|None = 33, queryparam: str|None = None):
    r = {'param': param + 1000}
    if queryparam:
        r.update({'query': queryparam})
    return r


class Object(BaseModel):
    obj_id: int
    name: str
    desc: str | None = None

@app.post('/demo/post-with-body')
async def post_demo(obj: Object)
    if obj.desc and len(obj.desc) > 100:
        return JSONResponse(status_code=400, content={'error': 'description too long'})


@app.get('/robots.txt')
async def robotstxt():
    return Response(content='Disallow: /', media_type='text/plain')
