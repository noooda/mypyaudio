import argparse
import logging


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


def setup_logger(
    log_level: int = logging.INFO, log_file: str = 'app.log'
) -> logging.Logger:
    logging.basicConfig(
        level=log_level,
        format='%(asctime)s - %(levelname)s - %(message)s',
        filename=log_file,
        filemode='a',
    )
    return logging.getLogger()
