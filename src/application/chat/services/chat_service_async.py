from abc import ABC, abstractmethod
from typing import Optional

from src.application.chat.dtos.begin_chat_request_dto import BeginChatRequestDto
from src.application.chat.dtos.conversation_request_dto import ConversationRequestDto
from src.application.chat.dtos.conversation_response_dto import ConversationResponseDto
from src.application.chat.dtos.conversation_summary_response_dto import ConversationSummaryResponseDto
from src.application.chat.dtos.send_message_request_dto import SendMessageRequestDto


class ChatServiceAsync(ABC):
    @abstractmethod
    async def begin_chat_async(self, request: BeginChatRequestDto) -> ConversationResponseDto:
        pass

    @abstractmethod
    async def get_user_summary_conversations_async(self, user_id: str) -> list[ConversationSummaryResponseDto]:
        pass

    @abstractmethod
    async def get_conversation_async(self, conversation_request: ConversationRequestDto) -> Optional[ConversationResponseDto]:
        pass

    @abstractmethod
    async def send_message_async(self, message: SendMessageRequestDto):
        pass
