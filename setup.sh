#!/bin/bash
# Script para instalar dependências e configurar o ambiente no Termux

echo "[*] Atualizando pacotes..."
pkg update -y && pkg upgrade -y

echo "[*] Instalando pacotes necessários..."
pkg install -y python git tesseract termux-api

echo "[*] Instalando pip packages..."
pip install pytesseract pillow

echo "[*] Criando comando global 'mikawr'..."
echo -e '#!/data/data/com.termux/files/usr/bin/bash\npython ~/mika-cheat/main.py' > ~/bin/mikawr
chmod +x ~/bin/mikawr

echo "[*] Setup concluído! Para iniciar o cheat, rode: mikawr"
