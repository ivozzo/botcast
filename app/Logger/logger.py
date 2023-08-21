import logging


class Logger:
    def __init__(self, path, filename, level):
        self.path = path
        self.filename = filename
        self.level = level
        self.__init_logger_with_file(logging_level=level, path=path, filename=filename)

    def __init__(self, level):
        self.path = None
        self.filename = None
        self.level = level
        self.__init_logger_only_console(logging_level=level)

    def info(self, message):
        self.logger.info(message)

    def warn(self, message):
        self.logger.warn(message)

    def error(self, message):
        self.logger.error(message)

    def debug(self, message):
        self.logger.debug(message)

    def is_debug(self):
        if self.level == "DEBUG":
            return True
        return False

    def __init_logger_with_file(self, logging_level, path, filename):

        loggerDictionary = {"INFO": logging.INFO, "WARN": logging.WARN, "DEBUG": logging.DEBUG, "ERROR": logging.ERROR}

        logging.basicConfig(
            level=loggerDictionary[logging_level],
            format="%(asctime)s|[%(threadName)-12.12s]|[%(levelname)-5.5s]| %(message)s",
            handlers=[
                logging.FileHandler("{0}/{1}".format(path, filename)),
                logging.StreamHandler()
            ])

        self.logger = logging.getLogger()

    def __init_logger_only_console(self, logging_level):

        loggerDictionary = {"INFO": logging.INFO, "WARN": logging.WARN, "DEBUG": logging.DEBUG, "ERROR": logging.ERROR}

        logging.basicConfig(
            level=loggerDictionary[logging_level],
            format="%(asctime)s|[%(threadName)-12.12s]|[%(levelname)-5.5s]| %(message)s",
            handlers=[
                logging.StreamHandler()
            ])

        self.logger = logging.getLogger()
