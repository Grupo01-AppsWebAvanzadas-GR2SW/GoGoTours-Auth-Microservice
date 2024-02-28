from flask import render_template, request, redirect, url_for
from flask.views import MethodView
from injector import inject
from src.application.chat.services.chat_service_async import ChatServiceAsync
from src.application.chat.dtos.send_message_request_dto import SendMessageRequestDto


class ChatView(MethodView):
    @inject
    def __init__(self, chat_service: ChatServiceAsync):
        self._chat_service = chat_service

    async def get(self):
        user_id = request.args.get("user_id") or "123" # TODO: Get user id from session
        conversations_summaries = await self._chat_service.get_user_summary_conversations_async(user_id)
        return render_template("chat/chat.html", conversations_summaries=conversations_summaries)
