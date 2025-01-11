import requests

from src.application.interfaces import AudioFileWriter, AudioRepository
from src.exceptions import FetchAudioStreamError, WriteAudioFileError


class DownloadAudioUseCase:
    def __init__(
        self,
        audio_repository: AudioRepository,
        audio_file_writer: AudioFileWriter,
    ) -> None:
        self.audio_repository = audio_repository
        self.audio_file_writer = audio_file_writer

    def execute(self, url: str, file_path: str) -> None:
        try:
            audio_stream = self._get_audio_stream(url)
        except FetchAudioStreamError:
            raise
        try:
            self._write_audio_file(audio_stream, file_path)
        except (FetchAudioStreamError, WriteAudioFileError):
            raise

    def _get_audio_stream(self, url: str) -> requests.Response:
        return self.audio_repository.fetch_audio_stream(url)

    def _write_audio_file(
        self, stream: requests.Response, file_path: str
    ) -> None:
        self.audio_file_writer.write(stream, file_path)
