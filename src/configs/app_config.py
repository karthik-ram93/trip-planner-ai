class AppConfig:
    # Model configuration
    MODEL_NAME = "llama3.2:1b"

    # Generation parameters
    TEMPERATURE = 0.7
    MAX_LENGTH = 5000
    TOP_K = 50
    TOP_P = 0.9
    REPETITION_PENALTY = 1.2