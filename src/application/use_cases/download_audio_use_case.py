import requests

from src.application.interfaces import AudioRepository, BinaryWriter
from src.exceptions import FetchAudioStreamError, WriteAudioFileError


class DownloadAudioUseCase:
    def __init__(
        self,
        audio_repository: AudioRepository,
        binary_writer: BinaryWriter,
    ) -> None:
        self.audio_repository = audio_repository
        self.binary_writer = binary_writer

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
        self.binary_writer.write(stream, file_path)
