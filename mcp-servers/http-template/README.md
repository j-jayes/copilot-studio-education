# HTTP Template Server

This scaffold is reserved for the remote-hosted MCP example.

## Current state

- keeps one minimal tool for inspection
- defaults to `stdio` so it can run locally today
- marks the place where the final HTTP transport and hosting shape will be wired in

## Run

```powershell
uv run --directory .\mcp-servers\http-template http-template-server
```
