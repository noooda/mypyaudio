import argparse

from src.application.use_cases import DownloadAudioUseCase


class CommandHandler:
    def __init__(self, download_audio_use_case: DownloadAudioUseCase) -> None:
        self.download_audio_use_case = download_audio_use_case

    def _download(self, url: str, file_path: str) -> None:
        self.download_audio_use_case.execute(url, file_path)

    def call_action(self, args: argparse.Namespace) -> None:
        command = args.command
        options = vars(args)
        options.pop('command')
        try:
            target_action = getattr(self, f'_{command}')
        except AttributeError:
            raise NotImplementedError(
                f'Command "{command}" is not implemented'
            )
        target_action(**options)
