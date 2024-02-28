from typing import Generic, TypeVar, Optional, Callable
from google.cloud.firestore import AsyncClient
from src.domain.common.entities.base_entity import BaseEntity
from src.application.common.repositories.generic_repository_async import GenericRepositoryAsync
from injector import inject


ID = TypeVar("ID")
T = TypeVar("T", bound=BaseEntity)


class FirestoreGenericRepositoryAsync(GenericRepositoryAsync, Generic[T, ID]):
    @inject
    def __init__(self, firestore_client: AsyncClient, collection_name: str, entity_constructor: Callable[[], T]):
        self._firestore_client = firestore_client
        self._collection_name = collection_name
        self._entity_constructor = entity_constructor

    async def get_async(self, entity_id: ID) -> Optional[T]:
        document_ref = self._firestore_client.collection(self._collection_name).document(str(entity_id))
        document_snapshot = await document_ref.get()
        
        if document_snapshot.exists:
            entity = self._entity_constructor()
            entity_dict = document_snapshot.to_dict()
            entity_dict["id"] = entity_id
            entity.merge_dict(document_snapshot.to_dict())
            return entity
        
        return None

    async def list_async(self) -> list[T]:
        try:
            collection_ref = self._firestore_client.collection(self._collection_name)
            documents_stream = collection_ref.stream()
            entities = []

            async for document_snapshot in documents_stream:
                data = document_snapshot.to_dict()
                data["id"] = document_snapshot.id
                entity = self._entity_constructor()
                entity.merge_dict(data)
                entities.append(entity)

            return entities
        except Exception:
            return []

    async def add_async(self, item: T) -> None:
        document_ref = self._firestore_client.collection(self._collection_name).document()
        await document_ref.set(item.to_dict())

    async def add_many_async(self, items: list[T]) -> None:
        batch = self._firestore_client.batch()
        collection_ref = self._firestore_client.collection(self._collection_name)

        for item in items:
            document_ref = collection_ref.document()
            batch.set(document_ref, item.to_dict())

        await batch.commit()

    async def update_async(self, item: T) -> None:
        document_ref = self._firestore_client.collection(self._collection_name).document(str(item.id))
        await document_ref.update(item.to_dict())

    async def update_many_async(self, items: list[T]) -> None:
        batch = self._firestore_client.batch()
        collection_ref = self._firestore_client.collection(self._collection_name)

        for item in items:
            document_ref = collection_ref.document(str(item.id))
            batch.update(document_ref, item.to_dict())

        await batch.commit()

    async def delete_async(self, item: T) -> None:
        document_ref = self._firestore_client.collection(self._collection_name).document(str(item.id))
        await document_ref.delete()

    async def delete_many_async(self, items: list[T]) -> None:
        batch = self._firestore_client.batch()
        collection_ref = self._firestore_client.collection(self._collection_name)

        for item in items:
            document_ref = collection_ref.document(str(item.id))
            batch.delete(document_ref)

        await batch.commit()

    async def delete_by_id_async(self, entity_id: ID) -> None:
        document_ref = self._firestore_client.collection(self._collection_name).document(str(entity_id))
        await document_ref.delete()

    async def exists_async(self, entity_id: ID) -> bool:
        document_ref = self._firestore_client.collection(self._collection_name).document(str(entity_id))
        document_snapshot = await document_ref.get()
        return document_snapshot.exists
