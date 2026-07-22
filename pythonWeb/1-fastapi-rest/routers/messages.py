from typing import List, Optional
from fastapi import APIRouter, Query
from fastapi.params import Depends

from models.message import Message
from services.message_service import MessageService
from dependencies.message_dependencies import get_message_service


router = APIRouter()

@router.get('/', response_model=List[Message])
def list_messages(service: MessageService = Depends(get_message_service)):
  return service.find_all()

@router.get('/{message_id}', response_model=Optional[Message])
def get_message(message_id: int, service: MessageService = Depends(get_message_service)):
  return service.find_by_id(message_id)

@router.get('/details/', response_model=Optional[Message])
def get_message_url_param(id: int = Query(..., ge=1), service: MessageService = Depends(get_message_service)):
  return service.find_by_id(id)