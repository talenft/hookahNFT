import fire
import logging
import pathlib
import cv2
import numpy
import os
import random

import project_config
import image_utils
from logging_config import CustomFormatter


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

    @staticmethod
    def _manipulate_hookah(hookah_image: numpy.ndarray):
        image_utils.paint_picture(hookah_image)
        return hookah_image

    def generate_hookah(self, base_hookah_path: pathlib.PurePath, dest_hookah_path: pathlib.PurePath):
        self.logger.debug("got command generate_hookah")

        if not os.path.exists(base_hookah_path):
            self.logger.error("base hookah file does not exist")
            return

        try:
            base_hookah_file = cv2.imread(str(base_hookah_path))
            print(type(base_hookah_file))
            image_utils.show_image(base_hookah_file)
            manupulated_hookah = self._manipulate_hookah(base_hookah_file)
            image_utils.show_image(manupulated_hookah)
            cv2.imwrite(str(dest_hookah_path), manupulated_hookah)
        except cv2.error:
            raise()


if __name__ == '__main__':
    fire.Fire(HookahGenerator)
