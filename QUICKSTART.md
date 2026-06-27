# Quick Start Guide

Get the Image Generation MCP Server up and running in 3 minutes.

## Installation

```bash
# Install dependencies
pip install -e .

# Optionally, create a .env file (optional, uses defaults if not provided)
cp .env.example .env
```

## Run the Server

```bash
# Start the server
python -m image_gen_mcp
```

You should see:
```
Image Generation MCP Server running...
```

## Test with Examples

In another terminal:

```bash
# Run example usage
python example_usage.py
```

This will:
1. Generate a landscape image (1024x1024)
2. Generate pixel art (256x256)
3. Generate an image with a specific seed (512x512)

Generated images will be saved in `./generated_images/`

## Integration with Claude Code

### Option 1: Via ~/.claude/settings.json

1. Open `~/.claude/settings.json`
2. Add:
```json
{
  "mcpServers": {
    "image-gen-mcp": {
      "command": "python",
      "args": ["-m", "image_gen_mcp"],
      "env": {
        "IMAGE_OUTPUT_DIR": "./generated_images"
      }
    }
  }
}
```

3. Restart Claude Code

### Option 2: Via Claude Code CLI

```bash
# If you've added this to your MCP servers
claude code --mcp image-gen-mcp
```

## Next Steps

- Read [README.md](README.md) for detailed documentation
- Customize `IMAGE_OUTPUT_DIR` environment variable
- Explore different models: `flux`, `flux-pro`, `flux-realism`
- Check `src/image_gen_mcp/providers.py` to add more providers

## Common Issues

**"No module named 'mcp'"**
```bash
pip install mcp
```

**"Connection timeout"**
- Check your internet connection
- Try a simpler prompt
- Increase timeout in `src/image_gen_mcp/providers.py`

**"Permission denied" saving images**
- Ensure `./generated_images/` directory has write permissions
- Or change `IMAGE_OUTPUT_DIR` to a writable location

## Support

Check the [README.md](README.md) Troubleshooting section for more help.
