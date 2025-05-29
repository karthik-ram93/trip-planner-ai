class OutputProcessor:
    @staticmethod
    def process_response(response):
        """
        Processes the raw response from the model and structures it for display.
        """
        # Try to get 'content' as an attribute first, then as a dict key
        content = getattr(response, 'content', None)
        if content is None and isinstance(response, dict):
            content = response.get('content')
        if content:
            return content
        else:
            print(response)
            return "Sorry, I couldn't generate any suggestions. Please try again."