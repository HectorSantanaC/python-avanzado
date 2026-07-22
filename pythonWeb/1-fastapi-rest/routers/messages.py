from typing import List
from models.message import Message
from fastapi import APIRouter

sample_messages: List[Message] =  [
  Message(id=1, text='Hola Mundo Python con fastAPI'),
  Message(id=2, text='Sección de fastAPI en progreso...'),
  Message(id=3, text='Este es un mensaje de prueba!')
]

router = APIRouter()

@router.get('/', response_model=List[Message])
def list_messages():
  return sample_messages