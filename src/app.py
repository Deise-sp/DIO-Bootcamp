import streamlit as st
from azure.storage.blob import BlobServiceClient
from services.blob_service import BlobStorageService
from services.credit_card_service import CreditCardValidator  # Assuming correct import


def configure_interface():
    """
    Configures the Streamlit interface for uploading and processing an image.
    """
    st.title("upload de arquivo DIO - Desafio 1 - Azure - Fake Docs")

    uploaded_file = st.file_uploader("Escolha um arquivo", type=["jpg", "png", "jpeg"])

    if uploaded_file is not None:
       fileName = uploaded_file.name
    #enviar para o blob storage
    blob_url = BlobStorageService(arg1=uploaded_file, arg2=fileName)
    
    if blob_url:
      st.write(f"Arquivo {fileName} enviado com sucesso para o Azure Blob Storage")
      credt_card_info = CreditCardValidator(blob_url) #chamar a função de detecção de informações de cartão de crédito
      show_image_and_validation(blob_url, credt_card_info)
    else:
      st.write(f"Erro ao enviar o arquivo {fileName} para o Azure Blob Storage")

def show_image_and_validation(blob_url, credit_card_info):
  st.image(blob_url, caption="Imagem enviada", use_column_width=True)
  st.write("Resultado da Validação:")
  if credit_card_info and credit_card_info["card_name"]:
    st.markdown(f"<h1 style='color: green;'>Cartão valido</h1>", unsafe_allow_html=True)
    st.write(f"Nome do titular: {credit_card_info['card_name']}")
    st.write(f"Banco emissor: {credit_card_info['Bank_name']}")
    st.write(f"Data de validade: {credit_card_info['expiry_date']}")
  else:
    st.markdown(f"<h1 style='color: green;'>Cartão invalido</h1>", unsafe_allow_html=True)
    st.write("Este não é um cartão de credito válido")   

if __name__ == "__main__":
    configure_interface()