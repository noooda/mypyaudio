from abc import ABC, abstractmethod

import requests


class AudioFileWriter(ABC):
    @abstractmethod
    def write(self, stream: requests.Response, file_path: str) -> None:
        pass
