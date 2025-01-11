from unittest.mock import Mock

import pytest
import requests

from src.application.interfaces import AudioFileWriter, AudioRepository
from src.application.use_cases import DownloadAudioUseCase


@pytest.fixture
def mock_audio_repository(mocker: Mock) -> Mock:
    return mocker.Mock(spec=AudioRepository)


@pytest.fixture
def mock_audio_file_writer(mocker: Mock) -> Mock:
    return mocker.Mock(spec=AudioFileWriter)


def test_call_audio_repository(
    mock_audio_repository: Mock, mock_audio_file_writer: Mock
) -> None:
    download_audio_use_case = DownloadAudioUseCase(
        mock_audio_repository, mock_audio_file_writer
    )
    audio_repository_url = 'https://example.com/audio.mp3'
    download_audio_use_case._get_audio_stream(audio_repository_url)
    mock_audio_repository.fetch_audio_stream.assert_called_once_with(
        audio_repository_url
    )


def test_call_audio_file_writer(
    mocker: Mock, mock_audio_repository: Mock, mock_audio_file_writer: Mock
) -> None:
    download_audio_use_case = DownloadAudioUseCase(
        mock_audio_repository, mock_audio_file_writer
    )
    audio_file_path = 'path/to/audio.mp3'
    response = mocker.Mock(spec=requests.Response)
    download_audio_use_case._write_audio_file(response, audio_file_path)
    mock_audio_file_writer.write.assert_called_once_with(
        response, audio_file_path
    )


def test_execute(
    mocker: Mock, mock_audio_repository: Mock, mock_audio_file_writer: Mock
) -> None:
    download_audio_use_case = DownloadAudioUseCase(
        mock_audio_repository, mock_audio_file_writer
    )
    audio_stream = mocker.Mock(spec=requests.Response)
    mock_get_audio_stream = mocker.patch.object(
        DownloadAudioUseCase, '_get_audio_stream', return_value=audio_stream
    )
    mock_write_audio_file = mocker.patch.object(
        DownloadAudioUseCase, '_write_audio_file', return_value=None
    )
    audio_repository_url = 'https://example.com/audio.mp3'
    audio_file_path = 'path/to/audio.mp3'
    download_audio_use_case.execute(audio_repository_url, audio_file_path)
    mock_get_audio_stream.assert_called_once_with(audio_repository_url)
    mock_write_audio_file.assert_called_once_with(
        audio_stream, audio_file_path
    )
