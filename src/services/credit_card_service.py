
from azure.core.credentials import AzureKeyCredential
from azure.ai.documentintelligence import DocumentIntelligenceClient
from azure.ai.documentintelligence.models import AnalyzeDocumentRequest
from utils.config import Config

class CreditCardValidator:

    def __init__(self):
        """
        Initializes the credit card validator with Azure Document Intelligence credentials.
        """
        self.credential = AzureKeyCredential(Config.AZURE_DOC_INT_KEY)
        self.document_client = DocumentIntelligenceClient(
            Config.AZURE_DOC_INT_ENDPOINT, self.credential
        )

    def validate_card(self, card_url):
        """
        Extracts information from a credit card image using the specified URL.

        Args:
            card_url (str): The URL of the credit card image.

        Returns:
            dict: A dictionary containing extracted information, or None if an error occurs.
        """

        try:
            
            card_info = self.document_client.begin_analyze_document(
                "prebuilt-creditCard", AnalyzeDocumentRequest(url_source=card_url)
            )
            result = card_info.result()

            for document in result.documents:
                fields = document.get("fields", {})

                return {
                    "card_name": fields.get('CardHolerName', {}).get('content'),
                    "card_number": fields.get('CardNumber', {}).get('content'),
                    "expiry_date": fields.get('ExpirationDate', {}).get('content'),
                    "bank_name": fields.get('IssuingBank', {}).get('content'),
                }

        except Exception as e:
            print(f"Error extracting credit card information: {e}")
            return None

                    
