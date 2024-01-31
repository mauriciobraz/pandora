import os

from dotenv import load_dotenv
from typing import Optional, Type, TypeVar

load_dotenv()

T = TypeVar("T")


def get_env_variable(type: Type[T], name: str, default: Optional[T]) -> T:
    """Type-safe wrapper for `os.getenv`.

    Args:
        type (Type[T]): Type of the environment variable.
        name (str): Name of the environment variable to get.
        default (T): Default value if the environment variable is not set.

    Returns:
        T: Value of the environment variable.

    Usage:
        ```python
        from path.to.dotenv import get_env_variable

        # Get a string environment variable with a default value.
        get_env_variable(str, "ENVIRONMENT", "development")

        # Get an integer environment variable with a default value.
        get_env_variable(int, "PORT", 8000)
        ```
    """

    try:
        value = os.getenv(name, default)
        return type.__call__(value)
    except ValueError:
        raise ValueError(
            f"Environment variable '{name}' is not of type '{type.__name__}'."
        )
    except TypeError:
        raise TypeError(
            f"Environment variable '{name}' is not set and has no default value."
        )
