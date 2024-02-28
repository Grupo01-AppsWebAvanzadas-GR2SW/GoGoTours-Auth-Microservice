from typing import Optional
from injector import inject
from src.application.chat.dtos.begin_chat_request_dto import BeginChatRequestDto
from src.application.chat.dtos.conversation_request_dto import ConversationRequestDto
from src.application.chat.dtos.conversation_response_dto import ConversationResponseDto
from src.application.chat.dtos.conversation_summary_response_dto import ConversationSummaryResponseDto
from src.application.chat.dtos.message_response_dto import MessageResponseDto
from src.application.chat.repositories.conversations_repository_async import ConversationsRepositoryAsync
from src.application.chat.services.chat_service_async import ChatServiceAsync
from src.application.chat.dtos.send_message_request_dto import SendMessageRequestDto
from src.domain.chat.entities.conversation import Conversation
from src.domain.chat.entities.message import Message


class DefaultChatServiceAsync(ChatServiceAsync):
    @inject
    def __init__(self, conversations_repository_async: ConversationsRepositoryAsync, ):
        self._conversations_repository_async = conversations_repository_async

    async def begin_chat_async(self, request: BeginChatRequestDto) -> ConversationResponseDto:
        possible_conversation: Optional[Conversation] = await self._conversations_repository_async.get_conversation_between_users(
            request.customer_id, request.admin_id
        )
        if possible_conversation is not None:
            return ConversationResponseDto(
                conversation_id=possible_conversation.id,
                recipient_name="Admin",  # TODO: Get recipient name
                messages=[
                    MessageResponseDto(
                        text=message.text,
                        date_sent=message.created_at
                    )
                    for message in possible_conversation.messages
                ]
            )

        new_conversation = Conversation(customer_id=request.customer_id, admin_id=request.admin_id)
        await self._conversations_repository_async.add_async(new_conversation)
        new_conversation = await self._conversations_repository_async.get_conversation_between_users_async(
            request.customer_id, request.admin_id
        )
        recipient_name = "Admin"  # TODO: Get recipient name
        ConversationResponseDto(
            conversation_id=new_conversation.id,
            recipient_name=recipient_name,
            messages=[]
        )

    async def get_user_summary_conversations_async(self, user_id: str) -> list[ConversationSummaryResponseDto]:
        return [ConversationSummaryResponseDto(
            conversation_id=conversation.id,
            recipient_name="Admin",  # TODO: Get recipient name
            last_message=conversation.messages[-1].text,
            last_message_date=conversation.messages[-1].created_at
        ) for conversation in await self._conversations_repository_async.get_user_conversations_async(user_id)]

    async def get_conversation_async(self, conversation_request: ConversationRequestDto) -> Optional[ConversationResponseDto]:
        conversation: Optional[Conversation] = await self._conversations_repository_async.get_user_conversation_async(
            user_id=conversation_request.sender_id,
            conversation_id=conversation_request.conversation_id
        )
        if conversation is None:
            return None

        return ConversationResponseDto(
            conversation_id=conversation.id,
            recipient_name="Admin",  # TODO: Get recipient name
            messages=[
                MessageResponseDto(
                    text=message.text,
                    date_sent=message.created_at
                )
                for message in conversation.messages
            ]
        )

    async def send_message_async(self, message: SendMessageRequestDto):
        conversation: Optional[Conversation] = await self._conversations_repository_async.get_user_conversation_async(
            user_id=message.sender_id,
            conversation_id=message.conversation_id
        )
        if conversation is None:
            raise Exception("Conversation not found")

        conversation.messages.append(Message(
            text=message.message,
            sender_id=message.sender_id,
            conversation_id=message.conversation_id
        ))

        await self._conversations_repository_async.update_async(conversation)
