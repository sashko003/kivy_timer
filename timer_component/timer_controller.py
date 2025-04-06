from threading import Thread

from timer_component.timer_view import TimerComponent


class TimerController:
    def __init__(self, timer_model):
        self._timer_model = timer_model
        self._timer_model.event_on_timeout = self.timeout_reached
        self._timer_model.event_refresh_timer = self.update_remaining_time
        self._ui = TimerComponent()
        self._ui.btn_start.bind(on_press=self.start_timer)
        self._ui.build()

    def start_timer(self, *args):
        interval = int(self._ui.ti_interval.text)
        if self.check_interval(interval):
            timer_thread = Thread(target=self._timer_model.start_timer, args=(interval,))
            timer_thread.start()
        else:
            self._ui.lbl_timer.text = "Invalid interval"

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

    @property
    def ui(self):
        return self._ui
