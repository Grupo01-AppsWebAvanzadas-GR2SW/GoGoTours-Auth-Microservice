from google.cloud.firestore import AsyncClient
from google.cloud import firestore
from injector import inject
from src.domain.reserves.entities.reserve import Reserve
from src.infrastructure.firebase.common.repositories.firestore_generic_repository_async import \
    FirestoreGenericRepositoryAsync
from src.application.reserves.repositories.reserve_repository_async import ReservesRepositoryAsync


class FirestoreReservesRepositoryAsync(FirestoreGenericRepositoryAsync[Reserve, str], ReservesRepositoryAsync):
    @inject
    def __init__(self, firestore_client: AsyncClient):
        super().__init__(firestore_client, 'reserves', Reserve)

    async def get_n_latest_reserves(self, n: int) -> list[Reserve]:
        docs_stream = self._firestore_client.collection('reserves').order_by(
            'created_at',
            direction=firestore.Query.DESCENDING
        ).limit(n).stream()
        reserves = []
        async for doc in docs_stream:
            reserve = Reserve()
            reserve.merge_dict(doc.to_dict())
            reserve.id = doc.id
            reserves.append(reserve)
        return reserves

    async def list_async(self) -> list[Reserve]:
        docs_stream = self._firestore_client.collection('reserves').stream()
        reserves = []
        async for doc in docs_stream:
            reserve = Reserve()
            reserve.merge_dict(doc.to_dict())
            reserve.id = doc.id
            reserves.append(reserve)
        return reserves


