from kivy.clock import Clock

from .timer import Timer
from abc import ABC, abstractmethod

import logging
LOG = logging.getLogger('common_logger')


class AbstractTimerModel(ABC):
    """
    Abstract class for timer model
    """
    @abstractmethod
    def start_timer(self, interval):
        """
        Use the instance of concrete timer to start execution
        :param interval: time in seconds
        :return:
        """
        pass

    @property
    @abstractmethod
    def remaining_time(self):
        """
        Time what is remaining till timeout
        :return:
        """
        pass


class TimerModel(AbstractTimerModel):
    """
    Timer model class
    """
    def __init__(self):
        self._timer = Timer()
        self._event_refresh_timer = None
        self._event_on_timeout = None
        self._event_on_exception = None
        self._timer_exception = None

    def start_timer(self, interval):
        """
        Use the instance of concrete timer to start execution
        :param interval: time in seconds
        :return:
        """
        LOG.debug("Starting timer with interval {}".format(interval))
        try:
            self._event_refresh_timer()  # start UI updates
            self._timer.start(interval) # start timer
            self._event_on_timeout() # notify about timeout
        except Exception as e:
            LOG.exception(f"Exception occured: {e}")
            self._timer_exception = f"Timer exception: {e}"
            self._event_on_exception() # notify about exception - display message on UI
        finally:
            LOG.debug("Finished timer with interval {}".format(interval))
            self._event_refresh_timer.cancel() # stop updating timer label

    @property
    def remaining_time(self):
        return self._timer.remaining_time

    @property
    def event_refresh_timer(self):
        return self._event_refresh_timer

    @event_refresh_timer.setter
    def event_refresh_timer(self, handler):
        """
        Sets handler to refresh UI based on Clock schedule
        :param handler: a method to update UI
        :return:
        """
        self._event_refresh_timer = Clock.create_trigger(handler, 0.1, interval=True)

    @property
    def event_on_timeout(self):
        return self._event_on_timeout

    @event_on_timeout.setter
    def event_on_timeout(self, handler):
        """
        Sets handler what should notify about timeout
        :param handler: a method for handling timeout
        :return:
        """
        self._event_on_timeout = Clock.create_trigger(handler, interval=False)

    @property
    def event_on_exception(self):
        return self._event_on_exception

    @event_on_exception.setter
    def event_on_exception(self, handler):
        """
        Sets handler what should notify about exception
        :param handler: a method for handling exception
        :return:
        """
        self._event_on_exception = Clock.create_trigger(handler, interval=False)

    @property
    def min_limit(self):
        return self._timer.MIN_LIMIT

    @property
    def max_limit(self):
        return self._timer.MAX_LIMIT

    @property
    def timer_exception(self):
        return self._timer_exception