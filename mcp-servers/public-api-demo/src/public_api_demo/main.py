from __future__ import annotations

from typing import Any

import httpx
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("public-api-demo")

NORDPOOL_BASE_URL = "https://dataportal-api.nordpoolgroup.com/api"


async def _get_json(url: str) -> dict[str, Any]:
    """Fetch JSON from a public endpoint with a short timeout."""
    async with httpx.AsyncClient(timeout=20.0) as client:
        response = await client.get(url)
        response.raise_for_status()
        return response.json()


@mcp.tool()
async def get_service_summary(topic: str) -> dict[str, str]:
    """Return a compact summary for a utility-oriented topic.

    This is a placeholder tool until the final public data source is selected.
    """
    summaries = {
        "electricity": "Electricity services often combine network, billing, and outage information.",
        "internet": "Internet services usually require clear guidance on availability, installation, and support.",
        "heating": "District heating questions often focus on coverage, maintenance, and seasonal usage.",
    }
    return {
        "topic": topic,
        "summary": summaries.get(topic.lower(), "No summary is defined for that topic yet."),
    }


@mcp.tool()
async def get_recent_day_ahead_context() -> dict[str, str]:
    """Return a basic status response for the future electricity-price demo tool.

    The class can replace this placeholder with a chosen public endpoint before delivery.
    """
    _ = NORDPOOL_BASE_URL
    return {
        "status": "placeholder",
        "next_step": "Bind this tool to the finalized public API before class delivery.",
    }


def main() -> None:
    """Start the demo server for local inspection."""
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
