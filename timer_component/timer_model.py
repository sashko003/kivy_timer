from kivy.clock import Clock

from .timer import Timer
from abc import ABC, abstractmethod

import logging
LOG = logging.getLogger('common_logger')


class AbstractTimerModel(ABC):
    @abstractmethod
    def start_timer(self, interval):
        pass

    @property
    @abstractmethod
    def remaining_time(self):
        pass


class TimerModel(AbstractTimerModel):
    def __init__(self):
        self._timer = Timer()
        self._event_refresh_timer = None
        self._event_on_timeout = None
        self._event_on_exception = None
        self._timer_exception = None

    def start_timer(self, interval):
        LOG.debug("Starting timer with interval {}".format(interval))
        try:
            self._event_refresh_timer()
            self._timer.start(interval)
            self._event_on_timeout()
        except Exception as e:
            LOG.exception(f"Exception occured: {e}")
            self._timer_exception = f"Timer exception: {e}"
            self._event_on_exception()
        finally:
            LOG.debug("Finished timer with interval {}".format(interval))
            self._event_refresh_timer.cancel()

    @property
    def remaining_time(self):
        return self._timer.remaining_time

    @property
    def event_refresh_timer(self):
        return self._event_refresh_timer

    @event_refresh_timer.setter
    def event_refresh_timer(self, handler):
        self._event_refresh_timer = Clock.schedule_interval(handler, 0.1)
        self._event_refresh_timer.cancel()

    @property
    def event_on_timeout(self):
        return self._event_on_timeout

    @event_on_timeout.setter
    def event_on_timeout(self, handler):
        self._event_on_timeout = Clock.schedule_once(handler)
        self._event_on_timeout.cancel()

    @property
    def event_on_exception(self):
        return self._event_on_exception

    @event_on_exception.setter
    def event_on_exception(self, handler):
        self._event_on_exception = Clock.schedule_once(handler)
        self._event_on_exception.cancel()

    @property
    def min_limit(self):
        return self._timer.MIN_LIMIT

    @property
    def max_limit(self):
        return self._timer.MAX_LIMIT

    @property
    def timer_exception(self):
        return self._timer_exception