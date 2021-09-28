import fire
import logging
import pathlib
import cv2
import os

import project_config
from logging_config import CustomFormatter

HOOKAH_SHOWCASE_WINDOW_NAME = "hookah window nigger"


class HookahGenerator:
    """
    The first hookah generator in our world lets go
    """

    def __init__(self):
        self.logger = logging.getLogger('game_handler')
        self._config_logger()

    def _config_logger(self):
        """
        configs the logger with level and colors and all that bullshit
        """
        self.logger.propagate = False
        self.logger.setLevel(logging.DEBUG if project_config.DEBUG else logging.INFO)
        logger_stream_handler = logging.StreamHandler()
        logger_stream_handler.setFormatter(CustomFormatter())
        self.logger.addHandler(logger_stream_handler)

    def generate_hookah(self, base_hookah_path: pathlib.PurePath, dest_hookah_path: pathlib.PurePath):
        self.logger.debug("got command generate_hookah")

        if not os.path.exists(base_hookah_path):
            self.logger.error("base hookah file does not exist")
            return

        try:
            base_hookah_file = cv2.imread(str(base_hookah_path))
            cv2.imshow(HOOKAH_SHOWCASE_WINDOW_NAME, base_hookah_file)
            cv2.waitKey()
            cv2.imwrite(str(dest_hookah_path), base_hookah_file)
        except cv2.error:
            raise()


if __name__ == '__main__':
    fire.Fire(HookahGenerator)
