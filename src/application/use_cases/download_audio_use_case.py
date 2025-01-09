from src.application.interfaces import AudioRepository, AudioWriter


class DownloadAudioUseCase:
    def __init__(
        self, audio_repository: AudioRepository, audio_writer: AudioWriter
    ) -> None:
        self.audio_repository = audio_repository
        self.audio_writer = audio_writer

    def execute(self, url: str, file_path: str) -> None:
        # TODO: FetchAudioErrorを補足する
        audio_data = self._download(url)
        # TODO: バイナリデータの保存処理を書く
        # TODO: WriteAudioFileErrorを補足する
        self._write(audio_data, file_path)

    def _download(self, url: str) -> bytes:
        return self.audio_repository.fetch_audio(url)

    def _write(self, audio_data: bytes, file_path: str) -> None:
        self.audio_writer.write_audio_file(audio_data, file_path)
