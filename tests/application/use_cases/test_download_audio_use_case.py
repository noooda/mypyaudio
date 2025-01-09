from unittest.mock import Mock

from src.application.interfaces import AudioRepository
from src.application.use_cases import DownloadAudioUseCase


def test_call_audio_repository(mocker: Mock) -> None:
    english_audio_repository = mocker.Mock(spec=AudioRepository)
    audio_repository_url = 'https://example.com/audio.mp3'
    download_audio_use_case = DownloadAudioUseCase(english_audio_repository)
    download_audio_use_case.execute(audio_repository_url)
    english_audio_repository.fetch_audio.assert_called_once_with(
        audio_repository_url
    )
