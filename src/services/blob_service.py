import os
import streamlit as st
from utils.config import Config  # Assuming correct import path
from azure.storage.blob import BlobServiceClient


class BlobStorageService:
    """Serviço para gerenciar o upload de arquivos para o Azure Blob Storage."""

    def __init__(self):
        """Inicializa o serviço com a string de conexão do Blob Storage."""
        blob_service_client = BlobServiceClient.from_connection_string(
            Config.AZURE_STORAGE_CONNECTION
        )

    def upload_blob(file, file_name):
        
        try:
            blob_service_client = BlobServiceClient.from_connection_string(
            Config.AZURE_STORAGE_CONNECTION
        )
            blob_client = blob_service_client.get_blob_client(
                container=Config.CONTAINER_NAME, blob=file_name)
            blob_client.upload_blob(file, overwrite=True)
            return blob_client.url
        except Exception as ex:
            st.error(f"Erro no upload para Blob Storage: {ex}")
            return None