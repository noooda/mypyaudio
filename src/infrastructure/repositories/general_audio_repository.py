import requests

from src.application.interfaces import AudioRepository
from src.exceptions import FetchAudioStreamError


class GeneralAudioRepository(AudioRepository):
    def __init__(self) -> None:
        pass

    def fetch_audio_stream(self, url: str) -> requests.Response:
        try:
            response = requests.get(url, stream=True)
            response.raise_for_status()
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
                f'{type(e).__name__}: Failed to fetch audio stream from {url}',
                status_code,
                reason,
            )
        return response
