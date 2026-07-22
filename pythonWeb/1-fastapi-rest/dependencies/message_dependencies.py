from services.message_service import MessageService, MessageServiceMemoryImpl

def get_message_service() -> MessageService:
  return MessageServiceMemoryImpl()