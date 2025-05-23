def load_words(lang):
    path = f"data/{lang}.txt"
    try:
        with open(path, "r") as f:
            return [w.strip().lower() for w in f if w.strip()]
    except FileNotFoundError:
        return []
      
