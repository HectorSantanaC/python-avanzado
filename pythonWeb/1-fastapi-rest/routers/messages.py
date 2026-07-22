from typing import List
from fastapi import APIRouter
from fastapi.params import Depends

from models.message import Message
from services.message_service import MessageService
from dependencies.message_dependencies import get_message_service


router = APIRouter()

@router.get('/', response_model=List[Message])
def list_messages(service: MessageService = Depends(get_message_service)):
  return service.find_all()