from unittest.mock import Mock

from src.application.interfaces import AudioRepository, AudioWriter
from src.application.use_cases import DownloadAudioUseCase


def test_call_audio_repository(mocker: Mock) -> None:
    english_audio_repository = mocker.Mock(spec=AudioRepository)
    english_audio_writer = mocker.Mock(spec=AudioWriter)
    audio_repository_url = 'https://example.com/audio.mp3'
    download_audio_use_case = DownloadAudioUseCase(
        english_audio_repository, english_audio_writer
    )
    download_audio_use_case._download(audio_repository_url)
    english_audio_repository.fetch_audio.assert_called_once_with(
        audio_repository_url
    )


def test_call_audio_writer(mocker: Mock) -> None:
    english_audio_repository = mocker.Mock(spec=AudioRepository)
    english_audio_writer = mocker.Mock(spec=AudioWriter)
    audio_file_path = 'path/to/audio.mp3'
    audio_data = b'audio data'
    download_audio_use_case = DownloadAudioUseCase(
        english_audio_repository, english_audio_writer
    )
    download_audio_use_case._write(audio_data, audio_file_path)
    english_audio_writer.write_audio_file.assert_called_once_with(
        audio_data, audio_file_path
    )


def test_execute(mocker: Mock) -> None:
    english_audio_repository = mocker.Mock(spec=AudioRepository)
    english_audio_writer = mocker.Mock(spec=AudioWriter)
    audio_repository_url = 'https://example.com/audio.mp3'
    audio_data = b'audio data'
    audio_file_path = 'path/to/audio.mp3'
    download_audio_use_case = DownloadAudioUseCase(
        english_audio_repository, english_audio_writer
    )
    mock_download = mocker.patch.object(
        DownloadAudioUseCase, '_download', return_value=audio_data
    )
    mock_write = mocker.patch.object(
        DownloadAudioUseCase, '_write', return_value=None
    )
    download_audio_use_case.execute(audio_repository_url, audio_file_path)
    mock_download.assert_called_once_with(audio_repository_url)
    mock_write.assert_called_once_with(audio_data, audio_file_path)
