import logging
import logging.handlers

class CustomFormatter(logging.Formatter):
    grey = "\x1b[38;20m"
    yellow = "\x1b[33;20m"
    red = "\x1b[31;20m"
    bold_red = "\x1b[31;1m"
    reset = "\x1b[0m"
    base_format = "[%(asctime)s] %(levelname)s %(name)s: %(message)s (%(filename)s:%(lineno)d)"

    def __init__(self, colored=True):
        super().__init__()
        self.colored = colored
        self.FORMATS = {
            logging.DEBUG: self.grey + self.base_format + self.reset,
            logging.INFO: self.grey + self.base_format + self.reset,
            logging.WARNING: self.yellow + self.base_format + self.reset,
            logging.ERROR: self.red + self.base_format + self.reset,
            logging.CRITICAL: self.bold_red + self.base_format + self.reset
        }

    def format(self, record):
        if self.colored:
            log_fmt = self.FORMATS.get(record.levelno, self.base_format)
        else:
            log_fmt = self.base_format
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)

def init_logger(name="logger", debug=False, colored=True, log_file="Test.log"):
    log = logging.getLogger(name)
    log.setLevel(logging.DEBUG)

    ConsoleHandler = logging.StreamHandler()
    ConsoleHandler.setLevel(logging.DEBUG if debug else logging.INFO)
    ConsoleHandler.setFormatter(CustomFormatter(colored=colored))
    log.addHandler(ConsoleHandler)

    FileHandler = logging.handlers.RotatingFileHandler(log_file)
    FileHandler.setLevel(logging.INFO)
    FileHandler.setFormatter(logging.Formatter("[%(asctime)s] %(levelname)s %(name)s: %(message)s (%(filename)s:%(lineno)d)"))
    log.addHandler(FileHandler)

    return log

if __name__ == "__main__":
    log = init_logger(debug=True, colored=True, log_file="Test.log")

    log.debug("debug message")
    log.info("info message")
    log.warning("warning message")
    log.error("error message")
    log.critical("critical message")