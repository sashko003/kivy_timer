from threading import Thread
from abc import ABC, abstractmethod

from timer_component.timer_view import TimerComponent

import logging
LOG = logging.getLogger('common_logger')


class AbstractTimerController(ABC):
    """
    Abstract class for timer controller
    """
    @abstractmethod
    def start_timer(self, *args):
        """
        Start timer execution.
        It is expected to be called on button press, that's why it takes additional arguments.
        :param args: instance of button what has been pressed
        :return:
        """
        pass

    @property
    @abstractmethod
    def ui(self):
        """
        :return: Returned ui (TimerComponent) instance
        """
        pass


class TimerController(AbstractTimerController):
    def __init__(self, timer_model):
        LOG.debug("Initializing timer controller")
        self._timer_model = timer_model
        # assign callbacks (events handlers) for specific events
        self._timer_model.event_on_timeout = self.timeout_reached
        self._timer_model.event_refresh_timer = self.update_remaining_time
        self._timer_model.event_on_exception = self.show_exception
        # creation of TimerComponent
        self._ui = TimerComponent()
        self._ui.build()
        # assigning handlers for Start button
        self._ui.btn_start.bind(on_press=self.start_timer)
        self._ui.btn_start.bind(on_press=self.disable_button)

    def start_timer(self, *args):
        """
        Checks set by user time interval.
        Calls timer execution using assigned instance of model.
        Updates UI accordingly.
        :param args: instance of button what has been pressed.
        :return:
        """
        LOG.debug("Timer started")
        try:
            # get time interval set by user
            interval = int(self._ui.ti_interval.text)
            if self.check_interval(interval):
                # create and start timer thread
                timer_thread = Thread(target=self._timer_model.start_timer, args=(interval,))
                timer_thread.start()
            else:
                # notify user about incorrect input
                self._ui.lbl_timer.text = (f"Invalid interval. Please use value from range "
                                           f"[{self._timer_model.min_limit}:{self._timer_model.max_limit}]")
                self.enable_button()
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
        """
        It is a callback what is used to update timer label.
        :param args: time spent from the last call, designed by Kivy
        :return:
        """
        self._ui.lbl_timer.text = f"{self._timer_model.remaining_time:.1f}"

    def timeout_reached(self, *args):
        """
        It is a callback what is used to update UI when timeout is reached.
        :param args: time spent from the last call, designed by Kivy
        :return:
        """
        self._ui.lbl_timer.text = "Timeout"
        self.enable_button()

    def check_interval(self, interval):
        """
        Just check if given interval is valid.
        :param interval: user input interval
        :return: True if interval is valid, False otherwise
        """
        if not (self._timer_model.min_limit <= interval <= self._timer_model.max_limit):
            return False
        else:
            return True

    def show_exception(self, *args):
        """
        It is a callback what is used to update UI in case of exception.
        :param args: time spent from the last call, designed by Kivy
        :return:
        """
        self._ui.lbl_timer.text = self._timer_model.timer_exception
        self.enable_button()

    @property
    def ui(self):
        return self._ui
