import argparse

from src.application.use_cases import DownloadAudioUseCase
from src.infrastructure.file import EnglishAudioFileWriter
from src.infrastructure.repositories import EnglishAudioRepository
from src.presentation.cli import CommandHandler


def main() -> None:
    parser = setup_argparse()
    args = parser.parse_args()

    command_handler = CommandHandler(
        download_audio_use_case=DownloadAudioUseCase(
            audio_file_writer=EnglishAudioFileWriter(),
            audio_repository=EnglishAudioRepository(),
        )
    )

    # TODO: エラーハンドリングを書く
    command_handler.call_action(args)


def setup_argparse() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser('pyaudio command handler')
    subparsers = parser.add_subparsers(
        dest='command', required=True, help='Available commands'
    )

    download_parser = subparsers.add_parser(
        'download', help='Download audio file'
    )
    download_parser.add_argument('url', type=str, help='URL of the audio file')
    download_parser.add_argument(
        'file_path', type=str, help='Path to save the downloaded audio file'
    )

    return parser


if __name__ == '__main__':
    main()
