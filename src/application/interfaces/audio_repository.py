from abc import ABC, abstractmethod


class AudioRepository(ABC):
    @abstractmethod
    def fetch_audio(self, url: str) -> bytes:
        pass
