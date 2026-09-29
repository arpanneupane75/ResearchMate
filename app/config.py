import os

from dotenv import load_dotenv


load_dotenv()


def get_required_env(name: str) -> str:
    """Get a required environment variable."""

    value = os.getenv(name)

    if not value or not value.strip():
        raise RuntimeError(
            f"Required environment variable '{name}' is missing."
        )

    return value.strip()


GEMINI_API_KEY = get_required_env("GEMINI_API_KEY")
TAVILY_API_KEY = get_required_env("TAVILY_API_KEY")