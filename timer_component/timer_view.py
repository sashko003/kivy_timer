from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

import logging
LOG = logging.getLogger('common_logger')


class TimerComponent(BoxLayout):
    """
    Basic UI representation for timer.
    It contains the following fields:
    - title: Label (optional)
    - field to set timer interval: TextInput
    - remaining time: Label
    - button to start timer: Button
    """
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
        """
        Creates all parts of TimerComponent
        :return: reference to self instance (configured TimerComponent)
        """
        LOG.debug("Building TimerComponent")
        self._build_component_title()
        self._build_textinput()
        self._build_timer_label()
        self._build_start_button()
        self.add_widget(self._lbl_title)
        self.add_widget(self._ti_interval)
        self.add_widget(self._lbl_timer)
        self.add_widget(self._btn_start)
        return self

    def _build_textinput(self):
        """
        Creates textinput widget for time interval
        :return:
        """
        self._ti_interval = TextInput(hint_text=TimerComponent.DEFAULT_TEXTHINT)
        self._ti_interval.font_size = TimerComponent.DEFAULT_TEXTINPUT_FONT_SIZE
        self._ti_interval.multiline = False
        self._ti_interval.input_filter = 'int'
        self._ti_interval.halign = 'center'
        self._ti_interval.valign = 'center'

    def _build_start_button(self):
        """
        Creates Start button
        :return:
        """
        self._btn_start = Button(text=TimerComponent.START_BUTTON_TEXT)
        self._btn_start.font_size = TimerComponent.DEFAULT_START_BUTTON_FONT_SIZE

    def _build_timer_label(self):
        """
        Creates timer label to display remaining time
        :return:
        """
        self._lbl_timer = Label(text=TimerComponent.DEFAULT_TIMER_TEXT)
        self._lbl_timer.font_size = TimerComponent.DEFAULT_TIMER_FONT_SIZE

    def _build_component_title(self):
        """
        Creates title for timer
        :return:
        """
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