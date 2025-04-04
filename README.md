# Transcrição de Áudio WhatsApp

Um script em Python para converter e transcrever áudios de WhatsApp (formato .ogg) para texto utilizando a API do Google Speech Recognition.

## 📋 Descrição

Este script faz o seguinte:

1. Converte um arquivo de áudio do WhatsApp (.ogg) para o formato .wav
2. Transcrive o conteúdo do áudio utilizando a API do Google Speech Recognition
3. Salva a transcrição em um arquivo de texto

## 🔧 Pré-requisitos

- Python 3.6 ou superior
- Bibliotecas necessárias:
  - `speech_recognition`
  - `pydub`

## 📦 Instalação

1. Clone este repositório ou baixe o script
2. Instale as dependências:

```bash
pip install SpeechRecognition pydub
```

Nota: A biblioteca `pydub` requer o FFmpeg instalado no sistema para manipular arquivos de áudio.

### Instalando o FFmpeg:

- **Windows**: Baixe do site oficial e adicione ao PATH ou use o Chocolatey:
  ```
  choco install ffmpeg
  ```

- **macOS**: Use o Homebrew:
  ```
  brew install ffmpeg
  ```

- **Linux (Ubuntu/Debian)**:
  ```
  sudo apt update
  sudo apt install ffmpeg
  ```

## 🚀 Uso

1. Coloque o arquivo de áudio do WhatsApp na mesma pasta do script
2. Execute o script:

```bash
python audio_transcription.py
```

Por padrão, o script procura um arquivo chamado "WhatsApp Ptt 2025-04-04 at 00.42.38.ogg". Para usar um arquivo diferente, modifique a variável `ogg_path` no código.

## 📋 Saída

- A transcrição será exibida no console
- Um arquivo chamado "transcricao.txt" será criado contendo o texto transcrito

## ⚙️ Configurações

- **Idioma**: O script está configurado para o português brasileiro (`pt-BR`). Para alterar, modifique o parâmetro `language` na chamada `recognize_google`.

## 📊 Exemplo

```
🔊 Transcrição do Áudio:
 Olá pessoal, esta é uma mensagem de teste para o sistema de transcrição.

✅ Transcrição salva em 'transcricao.txt'
```

## 🛠️ Solução de Problemas

- **Erro de conversão**: Verifique se o FFmpeg está instalado corretamente
- **Erro de reconhecimento**: A qualidade do áudio afeta a precisão da transcrição
- **Erro de acesso à API**: Verifique sua conexão com a internet

## 📝 Observações

- A API do Google Speech Recognition tem limites de uso diário
- A precisão da transcrição depende da qualidade do áudio e da clareza da fala
- Para arquivos maiores, considere usar outras APIs como a AssemblyAI ou Whisper API# transcricao.py
