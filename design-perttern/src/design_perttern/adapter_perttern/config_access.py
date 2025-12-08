from typing import Any, Protocol


class Config(Protocol):
    def get(self, key: str, default: Any | None = None) -> Any | None:
        """
        Get a value from the config.
        """
