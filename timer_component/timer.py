import time
from abc import ABC, abstractmethod


class AbstractTimer(ABC):
    def __init__(self, interval=0):
        self._interval = interval
        self._remaining_time = 0

    @abstractmethod
    def start(self, interval):
        pass

    @abstractmethod
    def stop(self):
        pass

    @property
    def interval(self):
        return self._interval

    @interval.setter
    def interval(self, value):
        self._interval = value

    @property
    def remaining_time(self):
        return self._remaining_time


class Timer(AbstractTimer):
    MIN_LIMIT = 0
    MAX_LIMIT = 300

    def __init__(self, interval=0):
        super().__init__(interval)
        self._interval = 0
        self._remaining_time = 0
        self._is_running = False

    def start(self, interval):
        ongoing_time = 0
        start_time = time.perf_counter()
        self._is_running = True
        while ongoing_time < interval and self._is_running:
            ongoing_time = time.perf_counter() - start_time
            self._remaining_time = interval - round(ongoing_time, 3)

    def stop(self):
        self._is_running = False
