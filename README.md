# mika-cheat

Cheat automático para o jogo Bomb Party rodando no Termux (Android).

# Descrição

Este projeto oferece um script que detecta os dígrafos (em teste) exibidos no jogo Bomb Party e digita automaticamente uma palavra válida em português ou inglês, dependendo em que dicionário você está usando, facilitando o jogo.

Funciona manual, digitando os dígrafos e interação com o teclado do Termux para digitar automaticamente as respostas.

# Funcionalidades

- Suporte a português (pt) e inglês (en)  
- Configuração de delay entre digitações  
- Definição do tamanho mínimo e máximo das palavras a serem digitadas  
- Detecção do prefixo da palavra na tela via OCR (termux-screenshot + tesseract)  
- Fácil instalação via script setup.sh  
- Interface de menu para configurar e iniciar o cheat 

# Requisitos

- Android com Termux instalado  
- Acesso à internet para instalar dependências  

# Instalação

```bash
git clone https://github.com/mikaelwr/mika-cheat.git
cd mika-cheat
chmod +x setup.sh
./setup.sh
