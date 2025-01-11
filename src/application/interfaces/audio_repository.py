from abc import ABC, abstractmethod

import requests


class AudioRepository(ABC):
    @abstractmethod
    def fetch_audio_stream(self, url: str) -> requests.Response:
        pass
