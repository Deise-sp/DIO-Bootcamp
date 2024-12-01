import os
from dotenv import load_dotenv
load_dotenv()

class Config:
  CONTAINER_NAME: str = os.getenv ("cartoes")
  AZURE_STORAGE_CONNECTION_STRING: str = os.getenv ("iD6B3Wz9c1Qsw01QSGPL4zZK3t4BHM5/4KIWV4OcGGw9JelmuknE6TQDDt3o5XaJxQVuqqcZvmka+AStWc4hYw==")
  ENDPOINT: str = os.getenv("https://doc-dio-fraude-eastus-de001.cognitiveservices.azure.com/")
  SUBSCRIPTION_KEY: str = os.getenv ( "8IDwba1uK11hnjhezPG4xag9Ig4KiBaexADadgmBBUyaxm9spJYdJQQJ99AKACYeBjFXJ3w3AAALACOGPjpq")
