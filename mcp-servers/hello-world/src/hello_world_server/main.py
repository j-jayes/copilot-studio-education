from mcp.server.fastmcp import FastMCP

mcp = FastMCP("hello-world")


@mcp.tool()
def ping(name: str) -> str:
    """Return a simple greeting for the supplied name."""
    return f"Hello, {name}!"


def main() -> None:
    """Start the training server over stdio for local inspection."""
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
