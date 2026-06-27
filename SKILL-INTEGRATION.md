# Image Generation Skill Integration

This project includes an integrated **Image Generation Skill** available globally in Claude Code.

## 🎨 About the Skill

The image-gen skill provides two commands for generating images:

- **`/image-gen`** - Generate realistic images from text prompts
- **`/pixelart`** - Generate pixel art from text prompts

All images are automatically:
- ✅ Generated using the `image-gen-mcp` server
- ✅ Displayed inline in Claude Code
- ✅ Saved to `./generated_images/` folder

## 📍 Skill Location

The skill is installed globally at:
```
~/.claude/skills/image-gen/
```

It's automatically available in all projects without additional installation.

## 🚀 Quick Setup in This Project

To use the image generation skill with this project, run the setup script:

### Windows (PowerShell)
```powershell
# Run from project root
C:\Users\{user}\.claude\skills\image-gen\setup.ps1 -ProjectRoot .

# Then install dependencies
pip install -e .
```

### Mac/Linux (Bash)
```bash
# Run from project root
~/.claude/skills/image-gen/setup.sh .

# Then install dependencies
pip install -e .
```

## 📋 What the Setup Script Does

✅ Copies MCP source code (`src/image_gen_mcp/`)  
✅ Copies dependencies file (`pyproject.toml`)  
✅ Creates `.mcp.json` configuration  
✅ Creates `.claude/.mcp.json` configuration  
✅ Creates `./generated_images/` folder  

**Important:** The setup script only copies files that don't already exist, so it's safe to run multiple times.

## 💻 Usage Examples

Once set up, you can use the skill anywhere in Claude Code:

### Generate a Realistic Image
```
/image-gen a majestic mountain landscape at sunset with golden light, photorealistic, 4K quality
```

### Generate Pixel Art
```
/pixelart pixel art style, retro 8-bit knight fighting a dragon, fantasy adventure game
```

## 📁 Project Structure After Setup

After running the setup script, your project will have:

```
.
├── src/
│   └── image_gen_mcp/           ← MCP source code (copied by setup)
│       ├── __init__.py
│       ├── __main__.py
│       ├── server.py
│       └── providers.py
├── generated_images/             ← Image output folder (created by setup)
├── .mcp.json                      ← MCP config (created by setup)
├── .claude/
│   └── .mcp.json                 ← Alternative MCP config (created by setup)
├── pyproject.toml                ← Dependencies (copied by setup)
├── CLAUDE.md
├── SKILL-INTEGRATION.md           ← This file
└── ... (other project files)
```

## 🔧 Configuration

After setup, the MCP is configured with:

```json
{
  "mcpServers": {
    "image-gen-mcp": {
      "command": "python",
      "args": ["-m", "image_gen_mcp"],
      "cwd": ".",
      "env": {
        "IMAGE_OUTPUT_DIR": "./generated_images"
      }
    }
  }
}
```

This means:
- Images are generated using the local MCP server
- All images are saved to `./generated_images/`
- The server runs in the current project directory

## 📚 Full Documentation

For complete skill documentation, see:
```
~/.claude/skills/image-gen/README.md
```

For skill usage and commands, see:
```
~/.claude/skills/image-gen/SKILL.md
```

## ⚙️ Dependencies

The skill requires:
- Python 3.8+
- `mcp` - Model Context Protocol library
- `requests` - HTTP client for API calls
- `python-dotenv` - Environment variable management

Install with:
```bash
pip install -e .
```

## 🌐 API

The skill uses **Pollinations.ai** - a free AI image generation API (no API key required).

- Free to use
- No authentication needed
- Rate limits apply for free tier

## 🎯 Typical Workflow

1. Run setup script in project root
2. Install dependencies: `pip install -e .`
3. Use `/image-gen` or `/pixelart` commands in Claude Code
4. Images are automatically saved and displayed
5. Find saved images in `./generated_images/`

## 🐛 Troubleshooting

### Images not generating?
- Verify setup script completed successfully
- Check internet connection (uses Pollinations.ai API)
- Try with a simpler prompt

### MCP not available?
- Re-run the setup script
- Verify `pyproject.toml` was copied
- Check `.mcp.json` exists in project root

### "Permission denied" errors?
- Ensure `./generated_images/` is writable
- Or change `IMAGE_OUTPUT_DIR` in `.mcp.json`

## 📖 More Information

- **Skill GitHub:** Check `~/.claude/skills/image-gen/`
- **MCP Server:** This repository
- **API:** https://pollinations.ai

---

**Version:** 1.0  
**Last Updated:** June 27, 2026  
**Status:** Fully integrated and ready to use
