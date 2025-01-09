from src.application.interfaces import AudioRepository


class DownloadAudioUseCase:
    def __init__(self, audio_repository: AudioRepository) -> None:
        self.audio_repository = audio_repository

    def execute(self, url: str) -> bytes:
        return self.audio_repository.fetch_audio(url)
