import logging

from src.application.use_cases import DownloadAudioUseCase
from src.infrastructure.file import AudioFileWriter
from src.infrastructure.repositories import GeneralAudioRepository
from src.presentation.cli import CommandHandler
from src.utils import setup_argparse, setup_logger


def main() -> None:
    setup_logger()

    parser = setup_argparse()
    args = parser.parse_args()

    command_handler = CommandHandler(
        download_audio_use_case=DownloadAudioUseCase(
            binary_writer=AudioFileWriter(),
            audio_repository=GeneralAudioRepository(),
        )
    )

    command_handler.call_action(args)


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        logging.error(e)
        print('Application failed. Please check the logs.')
