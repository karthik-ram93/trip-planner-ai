class AppConfig:
    # Model configuration
    MODEL_NAME = "google/gemma-3-1b-it"
    # MODEL_NAME = "meta-llama/Llama-3.2-1B-Instruct"

    # Generation parameters
    TEMPERATURE = 0.7
    MAX_LENGTH = 5000
    TOP_K = 50
    TOP_P = 0.9
    REPETITION_PENALTY = 1.2
    DO_SAMPLE = True