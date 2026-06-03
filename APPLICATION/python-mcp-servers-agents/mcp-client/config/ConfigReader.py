import json
from pathlib import Path
from typing import Any


class ConfigReader:

    def __init__(self, config_path: str | Path) -> None:
        self.config_path = Path(config_path)
        if not self.config_path.exists():
            raise FileNotFoundError(
                f"Config file not found at: {self.config_path}"
            )

        try:
            with open(self.config_path, "r") as f:
                self.config = json.load(f)
        except json.JSONDecodeError as exc:
            raise ValueError(
                f"Invalid JSON format in {self.config_path}: {exc}"
            ) from exc
        except Exception as exc:
            raise RuntimeError(
                f"Failed to read config object in {self.config_path}"
            ) from exc

    def get(self, key: str, default: Any = None) -> Any:
        """Get a value by dot-notation key (e.g., 'srv1.url')."""
        parts = key.split(".")
        node = self.config

        for part in parts:
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