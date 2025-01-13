import requests

from src.application.interfaces import BinaryWriter
from src.exceptions import FetchAudioStreamError, WriteAudioFileError


class AudioFileWriter(BinaryWriter):
    def __init__(self) -> None:
        pass

    def write(self, stream: requests.Response, file_path: str) -> None:
        try:
            with open(file_path, "wb") as audio_file:
                for chunk in stream.iter_content(chunk_size=8192):
                    if chunk:
                        audio_file.write(chunk)
        except (
            requests.exceptions.HTTPError,
            requests.exceptions.ConnectionError,
            requests.exceptions.Timeout,
            requests.exceptions.URLRequired,
        ) as e:
            status_code = None
            reason = None
            if type(e.response) is requests.Response:
                status_code = e.response.status_code
                reason = e.response.reason
            raise FetchAudioStreamError(
                f'{type(e).__name__}: '
                'Failed to download chunk from audio stream',
                status_code,
                reason,
            )
        except (FileNotFoundError, PermissionError, OSError) as e:
            raise WriteAudioFileError(
                f'{type(e).__name__}: '
                f'Failed to write audio file to {file_path}'
            )
