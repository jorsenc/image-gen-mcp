#!/usr/bin/env python3
"""Test Pollinations.ai API endpoints"""

import requests
import json
from urllib.parse import quote

print("Investigando Pollinations.ai API...")
print()

# Test different formats
tests = [
    ("prompt en URL", "https://image.pollinations.ai/prompt/a%20red%20cat"),
    ("seed en params", "https://image.pollinations.ai/prompt/a%20red%20cat?seed=12345"),
    ("modelo en URL", "https://image.pollinations.ai/prompt/a%20red%20cat?model=flux-pro"),
]

for name, url in tests:
    try:
        print(f"Test: {name}")
        print(f"URL: {url}")
        r = requests.head(url, timeout=5, allow_redirects=True)
        print(f"Status: {r.status_code}")
        print()
    except Exception as e:
        print(f"Error: {str(e)[:60]}")
        print()

# Test con dos prompts diferentes
print("\n=== Comparar dos prompts ===")
print()

url1 = "https://image.pollinations.ai/prompt/a%20beautiful%20red%20cat?seed=1"
url2 = "https://image.pollinations.ai/prompt/a%20blue%20dog?seed=1"

try:
    print("Descargando imagen 1...")
    r1 = requests.get(url1, timeout=30)
    size1 = len(r1.content)
    print(f"Tamaño: {size1} bytes")

    print("Descargando imagen 2...")
    r2 = requests.get(url2, timeout=30)
    size2 = len(r2.content)
    print(f"Tamaño: {size2} bytes")

    print()
    print(f"Mismos datos: {r1.content == r2.content}")
    print(f"Tamaños iguales: {size1 == size2}")

except Exception as e:
    print(f"Error: {e}")
