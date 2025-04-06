from threading import Thread
from abc import ABC, abstractmethod

from timer_component.timer_view import TimerComponent

import logging
LOG = logging.getLogger('common_logger')


class AbstractTimerController(ABC):
    @abstractmethod
    def start_timer(self, *args):
        pass

    @property
    @abstractmethod
    def ui(self):
        pass


class TimerController(AbstractTimerController):
    def __init__(self, timer_model):
        LOG.debug("Initializing timer controller")
        self._timer_model = timer_model
        self._timer_model.event_on_timeout = self.timeout_reached
        self._timer_model.event_refresh_timer = self.update_remaining_time
        self._timer_model.event_on_exception = self.show_exception
        self._ui = TimerComponent()
        self._ui.build()
        self._ui.btn_start.bind(on_press=self.start_timer)
        self._ui.btn_start.bind(on_press=self.disable_button)

    def start_timer(self, *args):
        LOG.debug("Timer started")
        try:
            interval = int(self._ui.ti_interval.text)
            if self.check_interval(interval):
                timer_thread = Thread(target=self._timer_model.start_timer, args=(interval,))
                timer_thread.start()
            else:
                self._ui.lbl_timer.text = "Invalid interval"
        except ValueError as value_error:
            LOG.exception(value_error)
            self._ui.lbl_timer.text = f"Invalid user input: {value_error}"
            self.enable_button()
        except Exception as ex:
            LOG.exception(ex)
            self._ui.lbl_timer.text = f"Unexpected error: {ex}"
            self.enable_button()

    def disable_button(self, *args):
        self._ui.btn_start.disabled = True

    def enable_button(self, *args):
        self._ui.btn_start.disabled = False

    def update_remaining_time(self, *args):
        LOG.debug("update_remaining_time")
        self._ui.lbl_timer.text = f"{self._timer_model.remaining_time:.1f}"

    def timeout_reached(self, *args):
        LOG.debug("update_remaining_time")
        self._ui.lbl_timer.text = "Timeout"
        self.enable_button()

    def check_interval(self, interval):
        if not (self._timer_model.min_limit <= interval <= self._timer_model.max_limit):
            return False
        else:
            return True

    def show_exception(self, *args):
        self._ui.lbl_timer.text = self._timer_model.timer_exception
        self.enable_button()

    @property
    def ui(self):
        return self._ui
