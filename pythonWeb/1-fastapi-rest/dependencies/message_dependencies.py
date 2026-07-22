from services.message_service import MessageService
from services.message_service_memory_impl import MessageServiceMemoryImpl
# from functools import lru_cache

# @lru_cache
def get_message_service() -> MessageService:
  return MessageServiceMemoryImpl()