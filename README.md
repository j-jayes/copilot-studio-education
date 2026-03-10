# Copilot Studio Education

This repository packages the material for a one-day Copilot Studio course.

It combines:

- a Quarto website source project in `website/`
- rendered static output for GitHub Pages in `docs/`
- attendee-ready snippets in `attendee-assets/`
- Python MCP starter projects in `mcp-servers/`
- deployment notes for Azure Container Apps and Docker in `deployment/`

## Course Shape

- Morning track: first agent, file grounding, website grounding, MCP overview, publishing channels
- Afternoon track: VS Code setup, `uv`, Python MCP server walkthrough, inspector loop, Azure deployment, Copilot Studio connection

## Repository Layout

- `website/` - Quarto source pages and Revealjs decks
- `docs/` - rendered website output for GitHub Pages
- `attendee-assets/` - copy-and-paste prompts, instructions, and exercise metadata
- `mcp-servers/` - example MCP servers for the afternoon session
- `src/` - shared Python helpers used across examples
- `data/` - public datasets and cleaned teaching copies
- `deployment/` - container and Azure deployment scaffolds
- `.github/quarto-docs/` - curated Quarto reference notes with source URLs

## Local Commands

Render the Quarto site:

```powershell
quarto render .\website
```

Preview the Quarto site:

```powershell
quarto preview .\website
```

Run the minimal MCP example:

```powershell
uv run --directory .\mcp-servers\hello-world hello-world-server
```

Run the canonical afternoon demo scaffold:

```powershell
uv run --directory .\mcp-servers\public-api-demo public-api-demo
```

## Notes

- Keep the public repo anonymous and reusable.
- Do not name the specific client in website copy or sample assets.
- The current implementation pass focuses on scaffolding, structure, and reusable teaching assets.