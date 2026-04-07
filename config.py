from dotenv import load_dotenv
load_dotenv()


import os

class ENV_CONFIG:
    GROQ_API_KEY=os.getenv("GROQ_API_KEY")
    GROQ_MODEL=os.getenv("GROQ_MODEL")
    GOOGLE_API_KEY=os.getenv("GOOGLE_API_KEY")
    OPENAI_API_KEY=os.getenv("OPENAI_API_KEY")
    MISTRAL_API_KEY=os.getenv("MISTRAL_API_KEY")
    SARVAM_API_KEY=os.getenv("SARVAM_API_KEY")
    HUGGINGFACEHUB_ACCESS_TOKEN=os.getenv("HUGGINGFACEHUB_ACCESS_TOKEN")
    MISTRAL_AI_MODEL=os.getenv("MISTRAL_AI_MODEL")

