import whisper
import yt_dlp


class   AUDOTEXT:
    def __init__(self):
        pass


    def download_audio(self, url:str, start_time:str, end_time:str):
        """
        Descarga el audio de un video de YouTube.
        :param url: URL del video de YouTube
        :return: Nombre del archivo de audio descargado
        """
        # Options for downloading the audio
        opciones = {
            "format": "bestaudio/best",   
            "outtmpl": "%(title)s",       
            "postprocessors": [{
                "key": "FFmpegExtractAudio",        # Extract with FFmpeg
                "preferredcodec": "wav",            # To wav
                "preferredquality": "192",          # Quality (192 kbps)
                }],
            "postprocessor_args": [
                "-ss", start_time,  # Start at "00:26:23"
                "-to", end_time,  # End at "01:23:27"
                ],
            }
        # Download
        with yt_dlp.YoutubeDL(opciones) as ydl:
            info = ydl.extract_info(url, download=True)
            print("Descarga completada.")
            audio_file = f"{info['title']}.wav"
        
        return audio_file


    def transcribie_audio(self, audio:object):
        """
        Use Whisper to transcribe the audio.
        :param audio: Audio file
        :return: Transcription
        """
        model = whisper.load_model("medium")  # seleccion el modelo para la transcripcion
        result = model.transcribe(audio)   
        with open("transcripcion.txt", "w") as f:     # el resultado de la transcripcion se guarda en un archivo de textp 
            f.write(result["text"])
        print("Transcripcion Completa.")


    def transcribe(self, url:str, start_time:str, end_time:str):
        """
        Principal method to transcribe a video from YouTube.
        :param url: URL del video de YouTube
        :param start_time: Tiempo de inicio de la transcripción
        :param end_time: Tiempo de fin de la transcripción
        :return: Transcription
        """
        audio = self.download_audio(url, start_time, end_time)
        text_transcription = self.transcribie_audio(audio)
        return text_transcription