import time
import json
import subprocess
from words import load_words

CONFIG_FILE = "config.json"

def load_config():
    try:
        with open(CONFIG_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {
            "language": "pt",
            "delay": 1.0,
            "min_length": 2,
            "max_length": 20,
            "wpm": 120
        }

def save_config(config):
    with open(CONFIG_FILE, "w") as f:
        json.dump(config, f, indent=2)

def type_text(text, delay):
    for char in text:
        subprocess.run(["input", "text", char])
        time.sleep(delay)
    subprocess.run(["input", "keyevent", "66"])  # Press ENTER

def run_manual_mode(config, words):
    wpm = config["wpm"]
    delay = 60 / (wpm * 5)
    print(f"\n[Modo Manual] Velocidade: {wpm} WPM ({delay:.3f}s por caractere)")

    while True:
        try:
            digrafo = input("\nDigite o dígrafo (ou 'sair'): ").strip().lower()
            if digrafo == "sair":
                break
            candidatos = [w for w in words if digrafo in w and config["min_length"] <= len(w) <= config["max_length"]]
            if candidatos:
                palavra = candidatos[0]
                print(f"> Digitando: {palavra}")
                type_text(palavra, delay)
            else:
                print("Nenhuma palavra encontrada.")
        except KeyboardInterrupt:
            break

def menu():
    config = load_config()
    words = load_words(config["language"])

    while True:
        print("\n=== mika-cheat Bomb Party ===")
        print(f"1) Idioma (atual: {config['language']})")
        print(f"2) Delay entre digitações (atual: {config['delay']}s)")
        print(f"3) Tamanho mínimo da palavra (atual: {config['min_length']})")
        print(f"4) Tamanho máximo da palavra (atual: {config['max_length']})")
        print(f"5) WPM (atual: {config['wpm']})")
        print("6) Iniciar Modo Manual (sem OCR)")
        print("7) Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            config["language"] = input("Idioma (pt/en): ").strip()
        elif escolha == "2":
            config["delay"] = float(input("Delay entre digitações (ex: 0.1): ").strip())
        elif escolha == "3":
            config["min_length"] = int(input("Tamanho mínimo: ").strip())
        elif escolha == "4":
            config["max_length"] = int(input("Tamanho máximo: ").strip())
        elif escolha == "5":
            config["wpm"] = int(input("WPM desejado (80 a 190): ").strip())
        elif escolha == "6":
            save_config(config)
            run_manual_mode(config, words)
        elif escolha == "7":
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    menu()
            
