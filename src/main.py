import sys, os

# Optionally set your HF cache location
os.environ['HF_HOME'] = 'D://huggingface/cache'
os.environ['HF_HUB_CACHE'] = 'D://huggingface/cache'
# os.environ['TRANSFORMERS_CACHE'] = 'D://huggingface/cache'


from configs.app_config import AppConfig  # Import the configuration
from services.trip_planner import TripPlanner
from models.huggingface_model import HuggingFaceModel
from services.output_processor import OutputProcessor
from utils.helpers import validate_query
from constants.app_constants import USER_ROLE


def main():
    print("Welcome to Trip Planner AI!")
    print("Getting the application ready ....!")

    # Initialize the HuggingFace model with the model name from AppConfig
    huggingface_model = HuggingFaceModel(model_name=AppConfig.MODEL_NAME)
    llm_model = huggingface_model.get_chat_instance()

    while True:
        user_query = input("Please enter your travel preferences or destination: ")
        validated_query = validate_query(user_query)

        # Use TripPlanner to construct messages
        trip_planner = TripPlanner()
        messages = trip_planner.construct_messages(validated_query, USER_ROLE) 

        print('Invoking LLM')
        # Send the messages to the chat instance
        response = llm_model.invoke(messages)

        # Process and display the response
        processed_output = OutputProcessor.process_response(response)
        print("\nHere are some suggestions for your trip:")
        print(processed_output)

        another = input("\nWould you like to ask another question? (yes/no): ").strip().lower()
        if another not in ("yes", "y"):
            print("Thank you for using Trip Planner AI. Safe travels!")
            break

if __name__ == "__main__":
    main()