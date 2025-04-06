from kivy.clock import Clock

from .timer import Timer


class TimerModel:
    def __init__(self):
        self._timer = Timer()
        self._event_refresh_timer = None
        self._event_on_timeout = None

    def start_timer(self, interval):
        self._event_refresh_timer()
        self._timer.start(interval)
        self._event_refresh_timer.cancel()
        self._event_on_timeout()

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
    def min_limit(self):
        return self._timer.MIN_LIMIT

    @property
    def max_limit(self):
        return self._timer.MAX_LIMIT