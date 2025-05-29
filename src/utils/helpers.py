import os
import getpass
# Placeholder for utility functions

def validate_query(query):
    if not query or len(query.strip()) == 0:
        return None
    else :
        return query.strip()

def format_suggestions(suggestions):
    if not suggestions:
        return "No suggestions available."
    formatted = "\n".join(f"- {suggestion}" for suggestion in suggestions)
    return f"Here are some suggestions for your trip:\n{formatted}"