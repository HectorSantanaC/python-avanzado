from typing import List
from fastapi import FastAPI
from pydantic import BaseModel

class Message(BaseModel):
    id: int
    text: str

app = FastAPI()

sample_messages: List[Message] =  [
  Message(id=1, text='Hola Mundo Python con fastAPI'),
  Message(id=2, text='Sección de fastAPI en progreso...'),
  Message(id=3, text='Este es un mensaje de prueba!')
]

@app.get('/')
def read_data():
  return {
    "message": 'Hola mundo! con FastAPI mi primer endponint!!!'
  }

@app.get('/messages', response_model=List[Message])
def list_messages():
  return sample_messages