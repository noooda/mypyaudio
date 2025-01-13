from abc import ABC, abstractmethod

import requests


class BinaryWriter(ABC):
    @abstractmethod
    def write(self, stream: requests.Response, file_path: str) -> None:
        pass
