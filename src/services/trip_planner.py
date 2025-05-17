from configs.prompts import *

class TripPlanner:
    def __init__(self):
        self.system_prompt = TRAVEL_ASSISTANT_SYSTEM_PROMPT_V1
        self.message_history = [ {"role": "system", "content": self.system_prompt} ]

    def construct_messages(self, content,role):
        """
        Constructs the messages list with a system prompt and user query.
        """
        self.message_history.append({"role": role, "content": content})
        return self.message_history