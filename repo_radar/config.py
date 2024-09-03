
import os

def load_config():
    return {
        'GITHUB_TOKEN': os.getenv('GITHUB_TOKEN'),
        'ANTHROPIC_API_KEY': os.getenv('ANTHROPIC_API_KEY'),
        'OPENAI_API_KEY': os.getenv('OPENAI_API_KEY'),
    }
