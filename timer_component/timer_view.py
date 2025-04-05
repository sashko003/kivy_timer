from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


class TimerComponent(BoxLayout):
    def __init__(self, **kwargs):
        super(TimerComponent, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.ti_interval = TextInput(text='Set time interval here')
        self.btn_start = Button(text='Start')
        self.lbl_timer = Label(text='000,000')
        self.lbl_title = Label(text='Kivy Timer')

    def build(self):
        self.add_widget(self.lbl_title)
        self.add_widget(self.ti_interval)
        self.add_widget(self.lbl_timer)
        self.add_widget(self.btn_start)