import sys, os

from configs.app_config import AppConfig  # Import the configuration
from services.trip_planner import TripPlanner
from services.output_processor import OutputProcessor
from utils.helpers import validate_query
from constants.app_constants import USER_ROLE, ASSISTANT_ROLE


def main():
    print("Welcome to Trip Planner AI!")
    print("Getting the application ready ....!")

    planner = TripPlanner()
    first_conversation = True

    while True:
        if first_conversation:
            user_query = input("Please enter your travel preferences or destination  : \n")
        else:
            user_query = input("Please provide your response or simply press Enter to exit  : \n")

        validated_query = validate_query(user_query)

        if not validated_query:
            print("Thank you for using Trip Planner AI. Safe travels!")
            break

        first_conversation = False

        response = planner.get_response(validated_query)
        print("\nModel Output : \n\n", response)

if __name__ == "__main__":
    main()