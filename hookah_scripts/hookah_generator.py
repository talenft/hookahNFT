import fire
import logging

import project_config
from logging_config import CustomFormatter


class HookahGenerator:

    def __init__(self):
        self.logger = logging.getLogger('game_handler')
        self._config_logger()

    def _config_logger(self):
        self.logger.propagate = False
        self.logger.setLevel(logging.DEBUG if project_config.DEBUG else logging.INFO)
        logger_stream_handler = logging.StreamHandler()
        logger_stream_handler.setFormatter(CustomFormatter())
        self.logger.addHandler(logger_stream_handler)

    def generate_hookah(self):
        self.logger.debug("got command generate_hookah")


if __name__ == '__main__':
    fire.Fire(HookahGenerator)
