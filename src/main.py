import sys, os

from configs.app_config import AppConfig  # Import the configuration
from services.trip_planner import TripPlanner
from models.huggingface_model import HuggingFaceModel
from services.output_processor import OutputProcessor
from utils.helpers import validate_query
from constants.app_constants import USER_ROLE, ASSISTANT_ROLE


def main():
    print("Welcome to Trip Planner AI!")
    print("Getting the application ready ....!")

    # Initialize the HuggingFace model with the model name from AppConfig
    huggingface_model = HuggingFaceModel(model_name=AppConfig.MODEL_NAME)
    llm_model = huggingface_model.get_chat_instance()

    first_conversation  = True
    trip_planner = None

    while True:
        if first_conversation:
            user_query = input("Please enter your travel preferences or destination  : \n")
            # Use TripPlanner to construct messages
            trip_planner = TripPlanner()
        else:
            user_query = input("Please provide your response or simply press Enter to exit  : \n")

        validated_query = validate_query(user_query)

        if not validated_query:
            print("Thank you for using Trip Planner AI. Safe travels!")
            break

        first_conversation = False
        messages = trip_planner.construct_messages(validated_query, USER_ROLE) 

        print('Invoking LLM')
        # Send the messages to the chat instance
        response = llm_model.invoke(messages)

        # Process and display the response
        processed_output = OutputProcessor.process_response(response)
        trip_planner.construct_messages(processed_output, ASSISTANT_ROLE) 
        print("\nHere are some suggestions for your trip:")
        print(processed_output)
            

if __name__ == "__main__":
    main()