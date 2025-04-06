from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

import logging
LOG = logging.getLogger('common_logger')


class TimerComponent(BoxLayout):
    DEFAULT_TEXTHINT = "Set time interval here"
    DEFAULT_TEXTINPUT_FONT_SIZE = 32
    DEFAULT_TITLE_FONT_SIZE = 32
    DEFAULT_TIMER_FONT_SIZE = 32
    DEFAULT_START_BUTTON_FONT_SIZE = 32
    START_BUTTON_TEXT = "Start"
    TITLE_TEXT = "Kivy Timer"
    DEFAULT_TIMER_TEXT = "0.0"

    def __init__(self, **kwargs):
        LOG.debug("Initializing TimerComponent")
        super(TimerComponent, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self._ti_interval = None
        self._lbl_timer = None
        self._btn_start = None
        self._lbl_title = None

    def build(self):
        LOG.debug("Building TimerComponent")
        self._build_component_title()
        self._build_textinput()
        self._build_timer_label()
        self._build_start_button()
        self.add_widget(self._lbl_title)
        self.add_widget(self._ti_interval)
        self.add_widget(self._lbl_timer)
        self.add_widget(self._btn_start)

    def _build_textinput(self):
        self._ti_interval = TextInput(hint_text=TimerComponent.DEFAULT_TEXTHINT)
        self._ti_interval.font_size = TimerComponent.DEFAULT_TEXTINPUT_FONT_SIZE
        self._ti_interval.multiline = False
        self._ti_interval.input_filter = 'int'

    def _build_start_button(self):
        self._btn_start = Button(text=TimerComponent.START_BUTTON_TEXT)
        self._btn_start.font_size = TimerComponent.DEFAULT_START_BUTTON_FONT_SIZE

    def _build_timer_label(self):
        self._lbl_timer = Label(text=TimerComponent.DEFAULT_TIMER_TEXT)
        self._lbl_timer.font_size = TimerComponent.DEFAULT_TIMER_FONT_SIZE

    def _build_component_title(self):
        self._lbl_title = Label(text=TimerComponent.TITLE_TEXT)
        self._lbl_title.font_size = TimerComponent.DEFAULT_TITLE_FONT_SIZE

    @property
    def ti_interval(self):
        if not self._ti_interval:
            self._build_textinput()
        return self._ti_interval

    @property
    def lbl_timer(self):
        if not self._lbl_timer:
            self._build_timer_label()
        return self._lbl_timer

    @property
    def btn_start(self):
        if not self._btn_start:
            self._build_start_button()
        return self._btn_start

    @property
    def lbl_title(self):
        if not self._lbl_title:
            self._build_component_title()
        return self._lbl_title