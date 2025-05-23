import os
import time
import json
import random
import subprocess
from ocr_utils import get_prefix

CONFIG_FILE = os.path.expanduser("~/.mika_cheat_settings.json")
DATA_DIR = os.path.expanduser("~/mika-cheat/data")
DEFAULT_CONFIG = {
    "language": "pt",
    "delay": 1.0,
    "min_len": 2,
    "max_len": 20,
}

def load_config():
    if not os.path.exists(CONFIG_FILE):
        save_config(DEFAULT_CONFIG)
    with open(CONFIG_FILE, "r") as f:
        return json.load(f)

def save_config(config):
    with open(CONFIG_FILE, "w") as f:
        json.dump(config, f)

def load_words(lang):
    path = os.path.join(DATA_DIR, f"palavras_{lang}.txt")
    if not os.path.exists(path):
        print(f"Arquivo de palavras {path} não encontrado.")
        return []
    with open(path, encoding="utf-8") as f:
        return [w.strip() for w in f.readlines() if w.strip()]

def choose_word(prefix, words, min_len, max_len):
    candidates = [w for w in words if w.startswith(prefix) and min_len <= len(w) <= max_len]
    if candidates:
        return random.choice(candidates)
    return None

def send_text(text):
    # Usa o termux-api para digitar no campo atual
    subprocess.run(["termux-clipboard-set", text])
    time.sleep(0.05)
    subprocess.run(["input", "keyevent", "66"])  # Enter
    time.sleep(0.1)
    subprocess.run(["input", "text", text])
    time.sleep(0.1)
    subprocess.run(["input", "keyevent", "66"])  # Enter

def menu():
    config = load_config()
    words = load_words(config["language"])

    while True:
        print("\n=== mika-cheat Bomb Party ===")
        print(f"1) Idioma (atual: {config['language']})")
        print(f"2) Delay entre digitações (atual: {config['delay']}s)")
        print(f"3) Tamanho mínimo da palavra (atual: {config['min_len']})")
        print(f"4) Tamanho máximo da palavra (atual: {config['max_len']})")
        print("5) Iniciar cheat")
        print("6) Sair")
        choice = input("Escolha uma opção: ").strip()

        if choice == "1":
            lang = input("Digite 'pt' para português ou 'en' para inglês: ").strip().lower()
            if lang in ["pt", "en"]:
                config["language"] = lang
                words = load_words(lang)
                save_config(config)
            else:
                print("Idioma inválido.")
        elif choice == "2":
            try:
                delay = float(input("Digite o delay entre digitações em segundos (ex: 1.0): ").strip())
                if delay >= 0:
                    config["delay"] = delay
                    save_config(config)
                else:
                    print("Delay deve ser >= 0.")
            except ValueError:
                print("Valor inválido.")
        elif choice == "3":
            try:
                min_len = int(input("Digite tamanho mínimo da palavra (>=2): ").strip())
                if min_len >= 2:
                    config["min_len"] = min_len
                    save_config(config)
                else:
                    print("Deve ser >= 2.")
            except ValueError:
                print("Valor inválido.")
        elif choice == "4":
            try:
                max_len = int(input("Digite tamanho máximo da palavra: ").strip())
                if max_len >= config["min_len"]:
                    config["max_len"] = max_len
                    save_config(config)
                else:
                    print("Deve ser >= tamanho mínimo.")
            except ValueError:
                print("Valor inválido.")
        elif choice == "5":
            print("Iniciando cheat... (Ctrl+C para parar)")
            try:
                run_cheat(config, words)
            except KeyboardInterrupt:
                print("\nCheat parado pelo usuário.")
        elif choice == "6":
            print("Saindo...")
            break
        else:
            print("Opção inválida.")

def run_cheat(config, words):
    print("Pressione Ctrl+C para parar.")
    while True:
        prefix = get_prefix()
        if not prefix:
            time.sleep(0.5)
            continue
        word = choose_word(prefix, words, config["min_len"], config["max_len"])
        if word:
            print(f"Prefixo: '{prefix}' -> digitando: {word}")
            send_text(word)
            time.sleep(config["delay"])
        else:
            print(f"Nenhuma palavra encontrada para prefixo '{prefix}'. Tentando novamente.")
            time.sleep(0.5)

if __name__ == "__main__":
    menu()
