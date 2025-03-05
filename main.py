from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles


app = FastAPI(title="US Population by year")

@app.get('/')
async def welcome() -> dict:
    return FileResponse('./index.html')

app.mount('/', StaticFiles(directory="/"), name="static")