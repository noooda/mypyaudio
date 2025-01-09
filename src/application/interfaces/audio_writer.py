from abc import ABC, abstractmethod


class AudioWriter(ABC):
    @abstractmethod
    def write_audio_file(self, data: bytes, file_path: str) -> None:
        pass
