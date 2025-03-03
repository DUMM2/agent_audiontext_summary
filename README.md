# agent_audiontext_summary

Este proyecto investiga las capacidades de resumen (Highlights) de agentes de IA en datos de audio y texto.

## Archivos

- `audio_to_text.py`: Este archivo contiene la clase `AUDOTEXT` que permite descargar audio de videos de YouTube y transcribirlo utilizando el modelo Whisper.
- `LICENSE`: Contiene la licencia Apache 2.0 bajo la cual se distribuye este proyecto.
- `README.md`: Este archivo que estás leyendo.

## Requisitos

Para instalar las dependencias del proyecto, ejecuta el siguiente comando:

```sh
pip install -r requirements.txt
```

Además, necesitas instalar `ffmpeg`. En macOS, puedes instalarlo usando Homebrew:, necesitas instalar `ffmpeg`. En macOS, puedes instalarlo usando Homebrew:, necesitas instalar `ffmpeg`. En macOS, puedes instalarlo usando Homebrew:

```sh
brew install ffmpegbrew install ffmpegbrew install ffmpeg
```

## Uso

### Clase AUDOTEXT

La clase `AUDOTEXT` proporciona los siguientes métodos:` proporciona los siguientes métodos:` proporciona los siguientes métodos:

- `download_audio(url: str, start_time: str, end_time: str)`: Descarga el audio de un video de YouTube en el intervalo de tiempo especificado.ad_audio(url: str, start_time: str, end_time: str)`: Descarga el audio de un video de YouTube en el intervalo de tiempo especificado.ad_audio(url: str, start_time: str, end_time: str)`: Descarga el audio de un video de YouTube en el intervalo de tiempo especificado.
- `transcribie_audio(audio: object)`: Transcribe el audio descargado utilizando el modelo Whisper.)`: Transcribe el audio descargado utilizando el modelo Whisper.)`: Transcribe el audio descargado utilizando el modelo Whisper.
- `transcribe(url: str, start_time: str, end_time: str)`: Método principal que descarga y transcribe el audio de un video de YouTube en el intervalo de tiempo especificado.- `transcribe(url: str, start_time: str, end_time: str)`: Método principal que descarga y transcribe el audio de un video de YouTube en el intervalo de tiempo especificado.- `transcribe(url: str, start_time: str, end_time: str)`: Método principal que descarga y transcribe el audio de un video de YouTube en el intervalo de tiempo especificado.

### Ejemplo de uso

```python
from audio_to_text import AUDOTEXT

audotext = AUDOTEXT()
transcription = audotext.transcribe("URL_DEL_VIDEO", "00:00:00", "00:01:00")
print(transcription)
```

## Licencia
Este proyecto está licenciado bajo la Licencia Apache 2.0. Consulta el archivo [`LICENSE`](LICENSE ) para más detalles.## Licencia```print(transcription)transcription = audotext.transcribe("URL_DEL_VIDEO", "00:00:00", "00:01:00")audotext = AUDOTEXT()from audio_to_text import AUDOTEXT```python