from abc import ABC, abstractmethod
from typing import Optional

from src.domain.chat.entities.conversation import Conversation
from src.application.common.repositories.generic_repository_async import GenericRepositoryAsync


class ConversationsRepositoryAsync(GenericRepositoryAsync[Conversation, str], ABC):
    @abstractmethod
    async def get_conversation_between_users_async(self, customer_id: str, admin_id: str) -> Optional[Conversation]:
        pass

    @abstractmethod
    async def get_user_conversations_async(self, user_id: str) -> list[Conversation]:
        pass

    @abstractmethod
    async def get_user_conversation_async(self, user_id: str, conversation_id: str) -> Optional[Conversation]:
        pass
