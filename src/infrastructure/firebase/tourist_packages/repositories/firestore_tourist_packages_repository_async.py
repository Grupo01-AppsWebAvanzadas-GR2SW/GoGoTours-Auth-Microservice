from google.cloud.firestore import AsyncClient
from google.cloud import firestore
from injector import inject
from src.domain.tourist_packages.entities.tourist_package import TouristPackage
from src.infrastructure.firebase.common.repositories.firestore_generic_repository_async import \
    FirestoreGenericRepositoryAsync
from src.application.tourist_packages.repositories.tourist_packages_repository_async import \
    TouristPackagesRepositoryAsync


class FirestoreTouristPackagesRepositoryAsync(FirestoreGenericRepositoryAsync[TouristPackage, str], TouristPackagesRepositoryAsync):
    @inject
    def __init__(self, firestore_client: AsyncClient):
        super().__init__(firestore_client, 'tourist_packages', TouristPackage)

    async def get_n_latest_packages(self, n: int) -> list[TouristPackage]:
        docs_stream = self._firestore_client.collection('tourist_packages').order_by(
            'created_at',
            direction=firestore.Query.DESCENDING
        ).limit(n).stream()
        packages = []
        async for doc in docs_stream:
            package = TouristPackage()
            package.merge_dict(doc.to_dict())
            package.id = doc.id
            packages.append(package)
        return packages

    async def list_async(self) -> list[TouristPackage]:
        docs_stream = self._firestore_client.collection('tourist_packages').stream()
        packages = []
        async for doc in docs_stream:
            package = TouristPackage()
            package.merge_dict(doc.to_dict())
            package.id = doc.id
            packages.append(package)
        return packages

    async def get_packages_by_start_date(self, start_date: str) -> list[TouristPackage]:
        docs_stream = self._firestore_client.collection('tourist_packages').where('start_date', '==', start_date).stream()
        packages = []
        async for doc in docs_stream:
            package = TouristPackage()
            package.merge_dict(doc.to_dict())
            package.id = doc.id
            packages.append(package)
        return packages

    async def get_by_name_async(self, name: str) -> TouristPackage:
        doc = await self._firestore_client.collection('tourist_packages').where('name', '==', name).get()
        package = TouristPackage()
        package.merge_dict(doc[0].to_dict())
        package.id = doc[0].id
        return package

    async def get_by_id_async(self, id: str) -> TouristPackage:
        doc = await self._firestore_client.collection('tourist_packages').where('id', '==', id).get()
        package = TouristPackage()
        package.merge_dict(doc[0].to_dict())
        package.id = doc[0].id
        return package
