#!/usr/bin/env python3
"""Investigar respuesta de Pollinations.ai"""

import requests

url = "https://image.pollinations.ai/prompt/a%20red%20cat"

try:
    r = requests.get(url, timeout=30)

    print(f"Status: {r.status_code}")
    print(f"Content-Type: {r.headers.get('content-type', 'N/A')}")
    print(f"Content-Length: {len(r.content)}")
    print()
    print(f"Primeros 500 bytes (decodificado):")
    print(r.text[:500])
    print()

    # Guardar para inspeccionar
    with open("test_response.bin", "wb") as f:
        f.write(r.content)
    print("Guardado en test_response.bin")

    # Verificar si es JSON
    try:
        json_data = r.json()
        print()
        print("Es JSON:")
        print(json_data)
    except:
        pass

except Exception as e:
    print(f"Error: {e}")
