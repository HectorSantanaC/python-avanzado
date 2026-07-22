from typing import List
from models.message import Message

class MessageService:

  def __init__(self):
    self.messages: List[Message] = [
      Message(id=1, text='Hola Mundo Python con fastAPI'),
      Message(id=2, text='Sección de fastAPI en progreso...'),
      Message(id=3, text='Este es un mensaje de prueba!'),
      Message(id=4, text='FastAPI con service'),
      Message(id=5, text='Inversión de control con Depends')
    ]

  def find_all(self) -> List[Message]:
    return self.messages