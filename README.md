# Image Generation MCP Server

A Model Context Protocol (MCP) server for generating images using Pollinations.ai. **No API key required** — completely free!

## Features

- 🎨 **Text-to-Image Generation** — Generate high-quality images from text prompts
- 🖼️ **Pixel Art Mode** — Specialized pixel art generation for retro/8-bit styles
- 🚀 **Multiple Models** — Support for Flux, Flux-Pro, and Flux-Realism
- 💾 **Auto-Save** — Generated images are automatically saved to disk
- 🆓 **Free** — Uses Pollinations.ai which requires no API key

## Installation

### Prerequisites
- Python 3.8 or higher
- pip

### Setup

1. **Clone or navigate to the project directory:**
   ```bash
   cd image-gen-mcp
   ```

2. **Install the package in development mode:**
   ```bash
   pip install -e .
   ```

3. **(Optional) Configure output directory:**
   Create a `.env` file in the project root:
   ```
   IMAGE_OUTPUT_DIR=./generated_images
   ```

## Usage

### Running the Server

```bash
python -m image_gen_mcp
```

The server will start and be ready to accept requests.

### Available Tools

#### 1. `generate_image`
Generate an image from a text prompt.

**Parameters:**
- `prompt` (required): Description of the image
- `width` (optional): Image width in pixels (default: 1024)
- `height` (optional): Image height in pixels (default: 1024)
- `model` (optional): Model to use - "flux", "flux-pro", or "flux-realism" (default: "flux")
- `seed` (optional): Random seed for reproducibility

**Example:**
```json
{
  "prompt": "a serene mountain landscape with a lake at sunset",
  "width": 1024,
  "height": 1024,
  "model": "flux"
}
```

#### 2. `generate_pixel_art`
Generate pixel art from a text prompt.

**Parameters:**
- `prompt` (required): Description of the pixel art
- `width` (optional): Image width in pixels (default: 256)
- `height` (optional): Image height in pixels (default: 256)

**Example:**
```json
{
  "prompt": "a knight with a sword and shield",
  "width": 256,
  "height": 256
}
```

#### 3. `list_providers`
List available image generation providers and their capabilities.

**Example:**
```json
{}
```

## Integration with Claude

To use this MCP with Claude Code, add it to your Claude configuration:

1. Edit `~/.claude/settings.json`
2. Add the MCP server configuration:

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

## Generated Images

By default, images are saved to `./generated_images/` with filenames like:
```
prompt_description_1719489264.png
```

You can change the output directory using the `IMAGE_OUTPUT_DIR` environment variable.

## Troubleshooting

### Connection Timeout
If you get a timeout error, it may be because:
- The image generation is taking longer than expected
- Your internet connection is unstable
- Pollinations.ai service is temporarily down

Try again or increase the timeout in `providers.py` (currently 120 seconds).

### Generation Failures
- Ensure you have a stable internet connection
- Try a simpler prompt
- Check that Pollinations.ai is accessible

## Architecture

```
image-gen-mcp/
├── src/image_gen_mcp/
│   ├── __init__.py
│   ├── __main__.py        # Entry point
│   ├── server.py          # MCP server implementation
│   └── providers.py       # Image generation providers
├── pyproject.toml         # Project configuration
└── README.md
```

## Contributing

Feel free to extend this server with:
- Additional image generation providers (Together AI, Hugging Face, etc.)
- Caching mechanisms
- Batch generation
- Image enhancement tools
- Cost tracking

## License

MIT License

## Disclaimer

This project uses Pollinations.ai for image generation. Make sure to comply with their terms of service and respect copyright and usage rights when generating images.
