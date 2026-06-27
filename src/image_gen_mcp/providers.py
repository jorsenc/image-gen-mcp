"""Image generation providers."""

import requests
import os
from pathlib import Path
from typing import Optional


class PollinationsProvider:
    """Pollinations.ai image generation provider (free, no API key required)."""

    BASE_URL = "https://image.pollinations.ai"

    @staticmethod
    def generate(
        prompt: str,
        width: int = 1024,
        height: int = 1024,
        seed: Optional[int] = None,
        model: str = "flux",
        output_dir: str = "./generated_images"
    ) -> str:
        """
        Generate an image using Pollinations.ai

        Args:
            prompt: Description of the image to generate
            width: Image width in pixels (default 1024)
            height: Image height in pixels (default 1024)
            seed: Random seed for reproducibility (optional)
            model: Model to use - 'flux', 'flux-pro', or 'flux-realism' (default 'flux')
            output_dir: Directory to save the image

        Returns:
            Path to the saved image file
        """
        # Create output directory if it doesn't exist
        Path(output_dir).mkdir(parents=True, exist_ok=True)

        # Build query parameters
        params = {
            "prompt": prompt,
            "width": width,
            "height": height,
            "model": model,
        }

        if seed is not None:
            params["seed"] = seed

        try:
            # Request image from Pollinations.ai using direct URL construction
            # Format: https://image.pollinations.ai/prompt/[prompt]?parameters
            encoded_prompt = prompt.replace(" ", "%20").replace("&", "%26")
            url = f"{PollinationsProvider.BASE_URL}/prompt/{encoded_prompt}"

            # Add parameters to URL
            param_str = "&".join([f"{k}={v}" for k, v in params.items() if k != "prompt"])
            if param_str:
                url += f"?{param_str}"

            response = requests.get(
                url,
                timeout=120,
                stream=True
            )
            response.raise_for_status()

            # Generate filename with safe characters
            import re
            import time
            prompt_slug = re.sub(r'[^a-z0-9_]', '', prompt[:30].replace(" ", "_").lower())
            if not prompt_slug:
                prompt_slug = "image"
            timestamp = int(time.time())
            filename = f"{prompt_slug}_{timestamp}.png"
            filepath = os.path.join(output_dir, filename)

            # Save image
            with open(filepath, "wb") as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)

            return filepath

        except requests.exceptions.RequestException as e:
            raise RuntimeError(f"Failed to generate image: {str(e)}")

    @staticmethod
    def generate_pixel_art(
        prompt: str,
        width: int = 256,
        height: int = 256,
        output_dir: str = "./generated_images"
    ) -> str:
        """
        Generate pixel art using Pollinations.ai with custom settings.

        Args:
            prompt: Description of the pixel art to generate
            width: Image width in pixels (default 256)
            height: Image height in pixels (default 256)
            output_dir: Directory to save the image

        Returns:
            Path to the saved image file
        """
        # Enhance prompt for pixel art style
        pixel_art_prompt = f"pixel art, retro, 8-bit style: {prompt}"

        return PollinationsProvider.generate(
            prompt=pixel_art_prompt,
            width=width,
            height=height,
            model="flux",
            output_dir=output_dir
        )

    @staticmethod
    def list_models() -> list[str]:
        """List available models."""
        return ["flux", "flux-pro", "flux-realism"]
