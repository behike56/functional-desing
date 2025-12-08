from bs4 import BeautifulSoup
from typing import Any


class XMLConfig:
    def __init__(self, bs: BeautifulSoup) -> None:
        self.bs = bs

    def get(self, key: str, default: Any | None = None) -> Any | None:
        """
        Get a value from the config.
        """
        value = self.bs.find(key)
        if value is None:
            return default
        return value.get_text()
