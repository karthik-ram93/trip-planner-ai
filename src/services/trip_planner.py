import json
import pprint
from configs.prompts import *
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from constants.app_constants import USER_ROLE,ASSISTANT_ROLE

class TripPlanner:
    def __init__(self):
        self.system_prompt = TRAVEL_ASSISTANT_SYSTEM_PROMPT_V3_1SHOT
        self.message_history = [ SystemMessage(content=self.system_prompt) ]

    def construct_messages(self, content,role):
        """
        Constructs the messages list with a system prompt and user query.
        """
        if role == USER_ROLE:
            message = HumanMessage(content=content)
        elif role == ASSISTANT_ROLE:
            message = AIMessage(content=content)
        else:
            raise ValueError("Invalid role. Use 'user' or 'assistant'.")
        self.message_history.append(message)
        
        # print (f'Constructed message: \n ')
        # pprint.pprint(self.message_history)
        return self.message_history