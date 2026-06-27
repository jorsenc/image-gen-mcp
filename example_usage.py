"""Example usage of the Image Generation MCP Server."""

import asyncio
import sys
from pathlib import Path

# Add src to path for development
sys.path.insert(0, str(Path(__file__).parent / "src"))

from image_gen_mcp.providers import PollinationsProvider


async def main():
    """Demonstrate image generation."""

    print("Image Generation MCP - Example Usage")
    print("=" * 50)

    # Example 1: Generate a regular image
    print("\n1. Generating a landscape image...")
    try:
        image_path = await asyncio.to_thread(
            PollinationsProvider.generate,
            prompt="a serene mountain landscape with a crystal-clear lake, sunset lighting",
            width=1024,
            height=1024,
            model="flux"
        )
        print(f"[OK] Image saved to: {image_path}")
    except Exception as e:
        print(f"[ERROR] {e}")

    # Example 2: Generate pixel art
    print("\n2. Generating pixel art...")
    try:
        image_path = await asyncio.to_thread(
            PollinationsProvider.generate_pixel_art,
            prompt="a brave knight with a sword and shield",
            width=256,
            height=256
        )
        print(f"[OK] Pixel art saved to: {image_path}")
    except Exception as e:
        print(f"[ERROR] {e}")

    # Example 3: Generate with custom seed
    print("\n3. Generating with reproducible seed...")
    try:
        image_path = await asyncio.to_thread(
            PollinationsProvider.generate,
            prompt="a futuristic robot in a neon city",
            width=512,
            height=512,
            model="flux-realism",
            seed=42
        )
        print(f"[OK] Image saved to: {image_path}")
    except Exception as e:
        print(f"[ERROR] {e}")

    # Example 4: List available models
    print("\n4. Available models:")
    models = PollinationsProvider.list_models()
    for model in models:
        print(f"   - {model}")

    print("\n" + "=" * 50)
    print("Examples completed! Check ./generated_images/ for results.")


if __name__ == "__main__":
    asyncio.run(main())
