class FetchAudioStreamError(Exception):
    def __init__(
        self,
        message: str,
        status_code: int | None = None,
        reason: str | None = None,
    ):
        status_code_section = f'[{status_code}] ' if status_code else ''
        reason_section = f' | {reason}' if reason else ''
        error_message = f'{status_code_section}{message}{reason_section}'
        super().__init__(error_message)


class WriteAudioFileError(Exception):
    pass
