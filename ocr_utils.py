import subprocess
import re

def get_prefix():
    # Tira screenshot da tela do Termux e salva como /sdcard/screencap.png
    subprocess.run(["termux-screenshot"])

    # Usa tesseract para extrair texto do screenshot
    result = subprocess.run(["tesseract", "/sdcard/screencap.png", "stdout"], capture_output=True, text=True)

    text = result.stdout.lower()

    # Extrai prefixo do texto, exemplo: palavra que está na tela (ajuste conforme layout do Bomb Party)
    match = re.search(r"\b([a-z]{2,})\b", text)
    if match:
        return match.group(1)
    return None
