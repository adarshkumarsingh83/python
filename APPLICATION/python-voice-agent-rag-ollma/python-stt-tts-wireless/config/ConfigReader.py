import json
import logging
from pathlib import Path
from typing import Any


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class ConfigReader:

    def __init__(self, config_path: str | Path) -> None:
        self._config_path = Path(config_path)
        self._config: dict[str, Any] = self._load()

    def _load(self) -> dict[str, Any]:
        if not self._config_path.is_file():
            raise FileNotFoundError(
                f"Config file not found: {self._config_path}"
            )
        try:
            with self._config_path.open("r", encoding="utf-8") as f:
                data = json.load(f)
        except json.JSONDecodeError as exc:
            raise ValueError(
                f"Invalid JSON in {self._config_path}: {exc}"
            ) from exc
        if not isinstance(data, dict):
            raise ValueError(
                f"Config root must be a JSON object in {self._config_path}"
            )
        return data

    def reload(self) -> None:
        """Reload configuration from disk."""
        self._config = self._load()

    @property
    def data(self) -> dict[str, Any]:
        """Return the full configuration dictionary."""
        return self._config

    def get(self, key: str, default: Any = None) -> Any:
        """Get a value by dot-notation key (e.g. `mcpServers.srv1.url`)."""
        node: Any = self._config
        for part in key.split("."):
            if isinstance(node, dict) and part in node:
                node = node[part]
            else:
                return default
        return node

    def require(self, key: str) -> Any:
        """Get a value by dot-notation key, raising `KeyError` if missing."""
        sentinel = object()
        value = self.get(key, sentinel)
        if value is sentinel:
            raise KeyError(f"Missing required config key: {key}")
        return value

    def __getitem__(self, key: str) -> Any:
        return self.require(key)

    def __contains__(self, key: str) -> bool:
        sentinel = object()
        return self.get(key, sentinel) is not sentinel