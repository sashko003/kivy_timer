import logging
import logging.handlers
import os


class LoggerCreator:
    """
    Class to create setup logger instance using logging package
    """
    def __init__(self, log_file=None):
        self.log_file = log_file
        self._logger = logging.getLogger('common_logger')
        self._logger.setLevel(logging.DEBUG)

    def config_file_logging(self):
        """
        Configure writing log to the file
        :return:
        """
        if self.log_file:
            if not os.path.exists(self.log_file):
                os.makedirs(os.path.dirname(self.log_file))
            file_handler = logging.FileHandler(self.log_file)
            file_handler.setLevel(logging.DEBUG)
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            file_handler.setFormatter(formatter)
            self._logger.addHandler(file_handler)

    def config_console_logging(self):
        """
        Configure writing log to the console
        :return:
        """
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        console_handler.setFormatter(formatter)
        self._logger.addHandler(console_handler)

    @property
    def logger(self):
        return self._logger

    @staticmethod
    def setup_default_logger():
        logger_creator = LoggerCreator('./logs/logs.log')
        logger_creator.config_file_logging()
        return logger_creator.logger
