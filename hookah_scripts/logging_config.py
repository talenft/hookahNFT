import logging
import colorama


class CustomFormatter(logging.Formatter):
    """Logging Formatter to add colors and count warning / errors"""

    white = colorama.Fore.WHITE
    yellow = colorama.Fore.YELLOW
    red = colorama.Fore.LIGHTRED_EX
    bold_red = colorama.Fore.RED
    reset = colorama.Fore.RESET
    format = "%(message)s"

    FORMATS = {
        logging.DEBUG: white + format + reset,
        logging.INFO: white + format + reset,
        logging.WARNING: yellow + format + reset,
        logging.ERROR: red + format + reset,
        logging.CRITICAL: bold_red + format + reset
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)
