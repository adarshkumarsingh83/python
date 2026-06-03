import logging
import os
from pathlib import Path

from .ConfigReader import ConfigReader

logger = logging.getLogger(__name__)

# Project root = parent of this `config` package directory.
PROJECT_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_CONFIG_PATH = PROJECT_ROOT / "resources" / "mcp-server.json"


class ApplicationConfig:
    """Application configuration loaded from a JSON file."""

    def __init__(self, config_path: str | Path | None = None) -> None:
        if config_path is None:
            env_path = os.getenv("APP_CONFIG_PATH")
            cfg_path = (
                Path(env_path) if env_path else DEFAULT_CONFIG_PATH
            )
        else:
            cfg_path = Path(config_path)

        # Resolve relative paths against the project root so the app works
        # regardless of the current working directory or OS.
        if not cfg_path.is_absolute():
            cfg_path = (PROJECT_ROOT / cfg_path).resolve()

        logger.info(f"Loading configuration from: {cfg_path}")
        self._reader = ConfigReader(cfg_path)

    def mcp_servers(self) -> dict[str, dict[str, str]]:
        """Return the individual MCP servers (`mcpServers`)."""
        return self._reader.get("mcp-list.mcpServers", {})

    def mcp_servers_config(self) -> dict[str, dict[str, dict[str, str]]]:
        """Return the full `mcp-list` configuration object."""
        return self._reader.get("mcp-list", {})