from typing import Optional

import bcrypt
from fastapi import Depends
from google.cloud.firestore import AsyncClient

from src.application.auth.repositories.users_repository_async import UsersRepositoryAsync
from src.domain.auth.entities.user import User
from src.infrastructure.firebase.common.repositories.firestore_generic_repository_async import \
    FirestoreGenericRepositoryAsync


class FirestoreUsersRepositoryAsync(FirestoreGenericRepositoryAsync[User, str], UsersRepositoryAsync):
    def __init__(self, firestore_client: AsyncClient = Depends(AsyncClient)):
        super().__init__(firestore_client, 'users', User)  # nombre de la colección

    async def get_user_by_email(self, email: str) -> Optional[User]:
        user_ref = self._firestore_client.collection('users').where('email', '==', email).limit(1)
        user_snapshot = await user_ref.get()

        for doc in user_snapshot:
            user_data = doc.to_dict()
            user_data["id"] = doc.id
            user = User()
            user.merge_dict(user_data)
            return user

        return None

    def password_matches(self, provided_password: str, hashed_password: str) -> bool:
        return bcrypt.checkpw(provided_password.encode('utf-8'), hashed_password.encode('utf-8'))

    async def create_user(self, user: User) -> User:
        user_data = user.to_dict()

        new_user_ref = self._firestore_client.collection('users').document()  # Firestore genera el ID
        await new_user_ref.set(user_data)

        user.entity_id = new_user_ref.id  # Actualiza el ID generado por Firestore en el objeto User
        return user

    async def get_user_by_reset_token(self, reset_token: str) -> Optional[User]:
        users_collection = self._firestore_client.collection('users').where('token', '==', reset_token)
        documents_stream = users_collection.stream()
        async for document in documents_stream:
            data = document.to_dict()
            data["id"] = document.id
            user = User()
            user.merge_dict(data)
            return user
        return None

    async def check_user_exists(self, email: str) -> bool:
        user_ref = self._firestore_client.collection('users').where('email', '==', email).limit(1)
        user_snapshot = await user_ref.get()
        return len(user_snapshot) > 0

    async def generate_reset_token(self, email):
        pass
