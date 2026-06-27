#!/usr/bin/env python3
"""Deep investigation of Pollinations.ai API"""

import requests
import json
from urllib.parse import urlencode

print("="*60)
print("INVESTIGANDO POLLINATIONS.AI API")
print("="*60)
print()

# Test 1: Different endpoint formats
print("TEST 1: Diferentes formatos de endpoint")
print("-" * 60)

test_urls = [
    # Format 1: /prompt/[prompt]
    ("URL con prompt en path", "https://image.pollinations.ai/prompt/red%20cat"),

    # Format 2: /generate con query params
    ("Query params", "https://image.pollinations.ai/generate?prompt=red+cat"),

    # Format 3: Con parámetros adicionales en URL
    ("Con params en URL", "https://image.pollinations.ai/prompt/red%20cat?seed=12345&width=512&height=512"),
]

for name, url in test_urls:
    try:
        print(f"\n{name}")
        print(f"URL: {url}")
        r = requests.head(url, timeout=10, allow_redirects=True)
        print(f"Status: {r.status_code}")
        if r.status_code == 200:
            print(f"[OK] Funciona")
        else:
            print(f"[ERROR] {r.status_code}")
    except Exception as e:
        print(f"[ERROR] {str(e)[:50]}")

# Test 2: Comparar respuestas con diferentes parámetros
print("\n\nTEST 2: Comparar prompts con parámetros")
print("-" * 60)

test_cases = [
    ("red cat", {"seed": "1"}),
    ("blue dog", {"seed": "1"}),
    ("red cat", {"seed": "2"}),
]

sizes = []
for prompt, params in test_cases:
    try:
        url = f"https://image.pollinations.ai/prompt/{prompt.replace(' ', '%20')}"
        if params:
            param_str = "&".join([f"{k}={v}" for k, v in params.items()])
            url += f"?{param_str}"

        print(f"\nPrompt: {prompt}, Params: {params}")
        r = requests.get(url, timeout=30)
        size = len(r.content)
        sizes.append((prompt, size))
        print(f"Tamaño: {size} bytes")
        print(f"Content-Type: {r.headers.get('content-type', 'N/A')}")

        # Guardar primera imagen para inspeccionar
        if len(sizes) == 1:
            with open("test_image_1.jpg", "wb") as f:
                f.write(r.content)
                print("Guardada en test_image_1.jpg")
        elif len(sizes) == 2:
            with open("test_image_2.jpg", "wb") as f:
                f.write(r.content)
                print("Guardada en test_image_2.jpg")

    except Exception as e:
        print(f"Error: {str(e)[:60]}")

# Test 3: Analizar estructura de respuesta
print("\n\nTEST 3: Analizar estructura JSON si aplica")
print("-" * 60)

try:
    url = "https://image.pollinations.ai/prompt/test%20image"
    r = requests.get(url, timeout=30)

    print(f"Status: {r.status_code}")
    print(f"Content-Type: {r.headers.get('content-type')}")
    print(f"Content-Length: {len(r.content)}")
    print(f"Headers: {dict(r.headers)}")

    # Intentar parsear como JSON
    try:
        data = r.json()
        print(f"\nES JSON:")
        print(json.dumps(data, indent=2)[:500])
    except:
        print(f"\nNo es JSON, es contenido binario (imagen)")
        print(f"Primeros 100 bytes: {r.content[:100]}")

except Exception as e:
    print(f"Error: {e}")

print("\n" + "="*60)
print("FIN DE INVESTIGACION")
print("="*60)
