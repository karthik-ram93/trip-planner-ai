from langchain_ollama import ChatOllama, OllamaEmbeddings
from configs.app_config import AppConfig  # Import AppConfig

class OllamaModel:
    def __init__(self, model_name=AppConfig.MODEL_NAME):

        self.llm = ChatOllama(
            model=model_name,
            temperature=AppConfig.TEMPERATURE,
            num_predict=AppConfig.MAX_LENGTH,
        )

    def get_chat_instance(self):
        return self.llm

def get_ollama_embedding_model():
    """
    Returns an OllamaEmbeddings instance for use in vector store embedding.
    """
    return OllamaEmbeddings(model="nomic-embed-text:v1.5")