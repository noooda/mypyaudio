import requests

from src.application.interfaces import AudioRepository


class EnglishAudioRepository(AudioRepository):
    def __init__(self) -> None:
        pass

    def fetch_audio(self, url: str) -> bytes:
        try:
            response = requests.get(url)
            response.raise_for_status()
        except requests.exceptions.HTTPError:
            # TODO: 例外処理を書く
            pass
        except requests.exceptions.ConnectionError:
            # TODO: 例外処理を書く
            pass
        except requests.exceptions.Timeout:
            # TODO: 例外処理を書く
            pass
        except requests.exceptions.URLRequired:
            # TODO: 例外処理を書く
            pass
        except requests.exceptions.TooManyRedirects:
            # TODO: 例外処理を書く
            pass
        return response.content
