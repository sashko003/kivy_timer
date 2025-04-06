import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.clock import Clock


class TimerApp(App):
    MIN_LIMIT = 0
    MAX_LIMIT = 300
    DEFAULT_FONT_SIZE = 32

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.interval = 0
        self.remaining_time = 0
        self.timer_event = None

        self.layout_main = None
        self.ti_interval = None
        self.lbl_timer = None
        self.btn_start = None

    def build(self):
        self.layout_main = BoxLayout(orientation='vertical')

        self.ti_interval = TextInput(hint_text="Enter time in seconds", multiline=False)
        self.ti_interval.input_filter = 'int'
        self.ti_interval.halign = 'center'
        self.ti_interval.valign = 'center'
        self.ti_interval.font_size = TimerApp.DEFAULT_FONT_SIZE

        self.lbl_timer = Label(text="0.0", font_size=TimerApp.DEFAULT_FONT_SIZE)

        self.btn_start = Button(text="Start", font_size=TimerApp.DEFAULT_FONT_SIZE)
        self.btn_start.bind(on_press=self.start_timer)

        self.layout_main.add_widget(self.ti_interval)
        self.layout_main.add_widget(self.lbl_timer)
        self.layout_main.add_widget(self.btn_start)

        return self.layout_main

    def start_timer(self, instance):
        try:
            self.interval = int(self.ti_interval.text)
            if not TimerApp.MIN_LIMIT <= self.interval <= TimerApp.MAX_LIMIT:
                self.lbl_timer.text = (f"Invalid input. Please use value in range "
                                       f"[{TimerApp.MIN_LIMIT}:{TimerApp.MAX_LIMIT}]")
                return
            self.remaining_time = self.interval
        except ValueError:
            self.lbl_timer.text = "Invalid input"
            return

        if self.timer_event:
            Clock.unschedule(self.timer_event)
        self.timer_event = Clock.schedule_interval(self.refresh_timer, 0.01)

    def refresh_timer(self, dt):
        self.remaining_time -= dt
        if self.remaining_time <= 0:
            self.remaining_time = 0
            self.lbl_timer.text = "Timeout"
            if self.timer_event:
                Clock.unschedule(self.timer_event)
        else:
            self.lbl_timer.text = f"{self.remaining_time:.1f}"


if __name__ == '__main__':
    TimerApp().run()