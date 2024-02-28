from typing import Optional
import firebase_admin
from firebase_admin import credentials, firestore_async
from google.cloud.firestore import AsyncClient


def initialize_firebase(credentials_file_path: str) -> None:
    cred = credentials.Certificate(credentials_file_path)
    if not firebase_admin._apps:
        firebase_admin.initialize_app(cred)


def get_firestore_async() -> AsyncClient:
    return firestore_async.client()
