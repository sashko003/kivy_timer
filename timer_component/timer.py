import time
from abc import ABC, abstractmethod

import logging
LOG = logging.getLogger('common_logger')


class AbstractTimer(ABC):
    """
    Abstract class for timer.
    """
    @abstractmethod
    def start(self, interval):
        pass

    @abstractmethod
    def stop(self):
        pass

    @property
    @abstractmethod
    def interval(self):
        pass

    @interval.setter
    @abstractmethod
    def interval(self, value):
        pass

    @property
    @abstractmethod
    def remaining_time(self):
        pass


class Timer(AbstractTimer):
    """
    Simple implementation of timer.
    """
    MIN_LIMIT = 0
    MAX_LIMIT = 300

    def __init__(self):
        self._interval = 0
        self._remaining_time = 0
        self._is_running = False

    def start(self, interval):
        """
        Starts counting
        :param interval: time in seconds to count down
        :return:
        """
        LOG.debug("Timer starting")
        ongoing_time = 0
        self._interval = interval
        start_time = time.perf_counter()
        self._is_running = True
        while ongoing_time < self._interval and self._is_running:
            ongoing_time = time.perf_counter() - start_time
            self._remaining_time = self._interval - ongoing_time
            time.sleep(0.05)
        self._is_running = False
        LOG.debug("Timer ended")

    def stop(self):
        self._is_running = False

    @property
    def interval(self):
        return self._interval

    @interval.setter
    def interval(self, value):
        self._interval = value

    @property
    def remaining_time(self):
        return self._remaining_time
