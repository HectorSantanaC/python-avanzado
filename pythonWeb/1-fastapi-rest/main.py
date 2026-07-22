from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def read_data():
  return {
    "message": 'Hola mundo! con FastAPI mi primer endponint!!!'
  }