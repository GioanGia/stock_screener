from fastai import FastAPI

app = FastAPI()

async def home(request):
    return {"hello": "world"}