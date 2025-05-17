from langchain_huggingface import ChatHuggingFace

from langchain_huggingface import HuggingFacePipeline
from configs.app_config import AppConfig  # Import AppConfig

from transformers import BitsAndBytesConfig

class HuggingFaceModel:
    def __init__(self, model_name=AppConfig.MODEL_NAME):

        # Generation parameters from AppConfig
        self.generation_params = {
            "temperature": AppConfig.TEMPERATURE,
            "max_length": AppConfig.MAX_LENGTH,
        }

        # quantization_config = BitsAndBytesConfig(
        # load_in_4bit=True,
        # bnb_4bit_quant_type="nf4",
        # bnb_4bit_compute_dtype="float16",
        # bnb_4bit_use_double_quant=True,
        # )

        self.llm = HuggingFacePipeline.from_model_id(
            model_id=model_name,
            task="text-generation",
            pipeline_kwargs=self.generation_params,
            # model_kwargs={"quantization_config": quantization_config},
        )

    def get_chat_instance(self):
        return ChatHuggingFace(llm = self.llm)