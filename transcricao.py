import os
import speech_recognition as sr
from pydub import AudioSegment

# Caminho do arquivo de áudio
ogg_path = "WhatsApp Ptt 2025-04-04 at 00.42.38.ogg"
wav_path = "audio.wav"

# Verificar se o arquivo existe
if not os.path.exists(ogg_path):
    print(f"Erro: Arquivo '{ogg_path}' não encontrado.")
    exit(1)

# Converter .ogg para .wav
try:
    audio = AudioSegment.from_file(ogg_path)
    audio.export(wav_path, format="wav")
except Exception as e:
    print(f"Erro ao converter áudio: {e}")
    exit(1)

# Inicializar reconhecimento
recognizer = sr.Recognizer()
try:
    with sr.AudioFile(wav_path) as source:
        audio_data = recognizer.record(source)
        text = recognizer.recognize_google(audio_data, language="pt-BR")
        print("Transcrição:", text)
except sr.UnknownValueError:
    print("Não foi possível entender o áudio.")
except sr.RequestError as e:
    print(f"Erro de requisição ao Google: {e}")
except Exception as e:
    print(f"Erro inesperado: {e}")
transcription_file = "transcricao.txt"

try:
    with sr.AudioFile(wav_path) as source:
        audio_data = recognizer.record(source)
        text = recognizer.recognize_google(audio_data, language="pt-BR")
        print("\n🔊 Transcrição do Áudio:\n", text)

        # Salvar no arquivo
        with open(transcription_file, "w", encoding="utf-8") as file:
            file.write(text)
        
        print(f"\n✅ Transcrição salva em '{transcription_file}'")
except sr.UnknownValueError:
    print("❌ Não foi possível entender o áudio.")
except sr.RequestError as e:
    print(f"❌ Erro de requisição ao Google: {e}")
except Exception as e:
    print(f"❌ Erro inesperado: {e}")
