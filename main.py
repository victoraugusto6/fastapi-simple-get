from fastapi import FastAPI
from datetime import datetime

app = FastAPI()


@app.get("/")
async def root():
    return {"horario": f'{datetime.today().hour}:{datetime.today().minute}'}

