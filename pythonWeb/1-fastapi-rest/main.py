from fastapi import FastAPI

app = FastAPI()

sample_messages: list[dict] =  [
  {
    'id': 1,
    'text': 'Hola Mundo Python con fastAPI'
  },
  {
    'id': 2,
    'text': 'Sección de fastAPI en progreso...'
  },
  {
    'id': 3,
    'text': 'Este es un mensaje de prueba!'
  },
]

@app.get('/')
def read_data():
  return {
    "message": 'Hola mundo! con FastAPI mi primer endponint!!!'
  }

@app.get('/messages')
def list_messages():
  return sample_messages