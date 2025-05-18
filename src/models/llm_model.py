from langchain_ollama import ChatOllama

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