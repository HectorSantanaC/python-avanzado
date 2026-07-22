from fastapi import FastAPI
from routers import messages

app = FastAPI()

app.include_router(messages.router, prefix='/messages', tags=['messages'])

@app.get('/')
def read_data():
  return {
    "message": 'Hola mundo! con FastAPI mi primer endponint!!!'
  }