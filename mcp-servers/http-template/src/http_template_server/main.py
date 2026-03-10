from __future__ import annotations

import os

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("http-template")


@mcp.tool()
def status() -> dict[str, str]:
    """Return a simple readiness payload for the template server."""
    return {
        "server": "http-template",
        "mode": os.getenv("MCP_TRANSPORT", "stdio"),
        "state": "ready",
    }


def main() -> None:
    """Start the template server.

    The initial scaffold defaults to stdio so it can be inspected locally.
    Replace the transport configuration with the finalized remote hosting shape
    before using this project as the Copilot Studio-connected example.
    """
    transport = os.getenv("MCP_TRANSPORT", "stdio")
    mcp.run(transport=transport)


if __name__ == "__main__":
    main()
