import logging

from src.application.use_cases import DownloadAudioUseCase
from src.infrastructure.file import EnglishAudioFileWriter
from src.infrastructure.repositories import EnglishAudioRepository
from src.presentation.cli import CommandHandler
from src.utils import setup_argparse, setup_logger


def main() -> None:
    setup_logger()

    parser = setup_argparse()
    args = parser.parse_args()

    command_handler = CommandHandler(
        download_audio_use_case=DownloadAudioUseCase(
            audio_file_writer=EnglishAudioFileWriter(),
            audio_repository=EnglishAudioRepository(),
        )
    )

    command_handler.call_action(args)


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        logging.error(e)
        print('Application failed. Please check the logs.')
