# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**Image Generation MCP Server** — A Model Context Protocol server that provides AI image generation capabilities to Claude using Pollinations.ai (free, no API key required).

The server exposes three tools:
- `generate_image` — Text-to-image generation with customizable dimensions and models (flux, flux-pro, flux-realism)
- `generate_pixel_art` — Specialized pixel art generation (256x256 by default)
- `list_providers` — Lists available providers and their capabilities

## Development Commands

### Installation
```bash
# Install the package in development mode with dependencies
pip install -e .

# Install with dev dependencies (testing, linting, formatting)
pip install -e ".[dev]"
```

### Running the Server
```bash
# Start the MCP server
python -m image_gen_mcp

# The server listens on stdio and is ready to accept MCP requests
```

### Testing & Development
```bash
# Run example usage (demonstrates all three tools)
python example_usage.py

# Run individual test files
python test_pollinations.py
python test_pollinations2.py

# Format code with Black
black src/

# Lint with Ruff
ruff check src/

# Run pytest (after installing dev dependencies)
pytest
```

## Architecture

**Single-Provider Pattern**: The server currently uses a single image provider (`PollinationsProvider`), but is designed for extensibility.

```
src/image_gen_mcp/
├── __main__.py      Entry point; calls server.main()
├── server.py        MCP server impl; defines tools and routes requests
├── providers.py     PollinationsProvider; handles API calls to Pollinations.ai
└── __init__.py
```

**Key Design Points**:
- `server.py` registers three MCP tools via `@app.list_tools()` and `@app.call_tool()` decorators
- `providers.py` contains `PollinationsProvider` with static methods for generating images and pixel art
- Generated images auto-save to `IMAGE_OUTPUT_DIR` (configurable via `.env` or environment variable)
- All generation calls are async-compatible using `asyncio.to_thread()` for blocking I/O

## Configuration

### Environment Variables
- `IMAGE_OUTPUT_DIR` — Directory where generated images are saved (default: `./generated_images`)

### Setup via .env
```bash
cp .env.example .env
# Edit .env to customize IMAGE_OUTPUT_DIR if needed
```

## Integration with Claude

To use this MCP in Claude Code, add to `~/.claude/settings.json`:
```json
{
  "mcpServers": {
    "image-gen-mcp": {
      "command": "python",
      "args": ["-m", "image_gen_mcp"],
      "cwd": "/path/to/image-gen-mcp",
      "env": {
        "IMAGE_OUTPUT_DIR": "./generated_images"
      }
    }
  }
}
```

Or from the test workspace (IMG-GEN-TEST) via its `.mcp.json`:
```json
{
  "mcpServers": {
    "image-gen-mcp": {
      "command": "python",
      "args": ["-m", "image_gen_mcp"],
      "cwd": "C:\\WORKSPACE\\IMG-GEN_MCP"
    }
  }
}
```

## Extending the Project

**To add a new provider**:
1. Create a new provider class in `providers.py` (e.g., `class HuggingFaceProvider`)
2. Implement `generate()` and `generate_pixel_art()` static methods
3. Update `server.py` to import and use the new provider

**To add a new tool**:
1. Define the tool schema in `list_tools()` with name, description, and inputSchema
2. Add handling in `call_tool()` to match the tool name and call the provider

## Dependencies

- **mcp** — Model Context Protocol library for server implementation
- **requests** — HTTP client for calling Pollinations.ai API
- **python-dotenv** — Loads environment variables from .env file
- **pytest, black, ruff** (dev) — Testing, formatting, and linting

## Known Limitations

- Pollinations.ai API calls are synchronous; the MCP server wraps them with `asyncio.to_thread()` to avoid blocking
- Timeout is currently 120 seconds; can be adjusted in `providers.py` if needed
- Free tier of Pollinations.ai may have rate limits; test with reasonable request spacing

## Troubleshooting

| Issue | Solution |
|-------|----------|
| "No module named 'mcp'" | `pip install mcp` |
| Connection timeout | Check internet, try simpler prompt, or increase timeout in `providers.py` |
| "Permission denied" saving images | Ensure `./generated_images/` exists and is writable, or change `IMAGE_OUTPUT_DIR` |
| Images not generating | Verify Pollinations.ai is accessible; check internet connection; try simpler prompts |

