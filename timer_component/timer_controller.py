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
        timer_thread = Thread(target=self._timer_model.start_timer, args=(interval,))
        timer_thread.start()

    def update_remaining_time(self, *args):
        self._ui.lbl_timer.text = f"{self._timer_model.remaining_time:.2f}"

    def timeout_reached(self, *args):
        self._ui.lbl_timer.text = "Timeout"

    @property
    def ui(self):
        return self._ui
