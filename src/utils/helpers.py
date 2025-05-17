import os
import getpass
# Placeholder for utility functions

def validate_query(query):
    if not query or len(query.strip()) == 0:
        raise ValueError("Query cannot be empty.")
    return query.strip()

def format_suggestions(suggestions):
    if not suggestions:
        return "No suggestions available."
    formatted = "\n".join(f"- {suggestion}" for suggestion in suggestions)
    return f"Here are some suggestions for your trip:\n{formatted}"

def check_hf_token():
    """
    Check if the Hugging Face token is set in the environment variable.
    If not, prompt the user to input it and set it.
    """
    hf_token_env_var = "HUGGINGFACEHUB_API_TOKEN"
    hf_token = os.getenv(hf_token_env_var)

    if not hf_token:
        print("Hugging Face token not found in environment variables.")
        os.environ[hf_token_env_var] = getpass.getpass(
    "Enter your Hugging Face API key: "
)
        print(f"Hugging Face token has been set in the environment variable")
    else:
        print("Hugging Face token found in environment variables.")