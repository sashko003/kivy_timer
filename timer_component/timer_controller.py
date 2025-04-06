from threading import Thread

from timer_component.timer_view import TimerComponent


class TimerController:
    def __init__(self, timer_model):
        self._timer_model = timer_model
        self._timer_model.event_on_timeout = self.timeout_reached
        self._timer_model.event_refresh_timer = self.update_remaining_time
        self._timer_model.event_on_exception = self.show_exception
        self._ui = TimerComponent()
        self._ui.btn_start.bind(on_press=self.start_timer)
        self._ui.build()

    def start_timer(self, *args):
        try:
            interval = int(self._ui.ti_interval.text)
            if self.check_interval(interval):
                timer_thread = Thread(target=self._timer_model.start_timer, args=(interval,))
                timer_thread.start()
            else:
                self._ui.lbl_timer.text = "Invalid interval"
        except ValueError as value_error:
            self._ui.lbl_timer.text = f"Invalid user input: {value_error}"
        except Exception as ex:
            self._ui.lbl_timer.text = f"Unexpected error: {ex}"

    def update_remaining_time(self, *args):
        print("update_remaining_time")
        self._ui.lbl_timer.text = f"{self._timer_model.remaining_time:.2f}"

    def timeout_reached(self, *args):
        print("update_remaining_time")
        self._ui.lbl_timer.text = "Timeout"

    def check_interval(self, interval):
        if not (self._timer_model.min_limit <= interval <= self._timer_model.max_limit):
            return False
        else:
            return True

    def show_exception(self, *args):
        self._ui.lbl_timer.text = self._timer_model.timer_exception

    @property
    def ui(self):
        return self._ui
