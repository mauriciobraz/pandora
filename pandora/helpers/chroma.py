from chromadb import HttpClient
from chromadb.config import Settings

from .dotenv import get_env_variable

chroma = HttpClient(
    settings=Settings(
        chroma_client_auth_provider="chromadb.auth.basic.BasicAuthClientProvider",
        chroma_client_auth_credentials=get_env_variable(
            str, "CHROMA_CLIENT_AUTH_CREDENTIALS", None
        ),
    ),
    port=get_env_variable(int, "CHROMA_PORT", 8000),  # type: ignore
    host=get_env_variable(str, "CHROMA_HOST", "localhost"),
)
