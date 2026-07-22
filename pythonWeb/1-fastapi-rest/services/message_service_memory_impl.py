from typing import List, Optional

from models.message import Message
from services.message_service import MessageService

class MessageServiceMemoryImpl(MessageService):

  def __init__(self):
    self.messages: List[Message] = [
      Message(id=1, text='Hola Mundo Python con fastAPI'),
      Message(id=2, text='Sección de fastAPI en progreso...'),
      Message(id=3, text='Este es un mensaje de prueba!'),
      Message(id=4, text='FastAPI con service'),
      Message(id=5, text='Inversión de control con Depends')
    ]

  def find_all(self) -> List[Message]:
    # print(f'ID del servicio: {id(self)}')
    return self.messages

  def find_by_id(self, message_id: int) -> Optional[Message]:
    message_found = next((msg for msg in self.messages if msg.id == message_id), None)
    return message_found