import kivy

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

import time
from threading import Thread


class MyApp(App):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical')
        self.textinput = TextInput(text='Set time interval here')
        self.btn1 = Button(text='Start')
        self.btn1.bind(on_press=self.start_timer)
        self.timer = Label(text='000,000')
        self.title_ = Label(text='Kivy Timer')

    def start_timer(self, instance):
        def _start_timer():
            interval = float(self.textinput.text)
            ongoing_time = 0
            start_time = time.perf_counter()
            while ongoing_time < interval:
                ongoing_time = time.perf_counter() - start_time
                left_time = interval - round(ongoing_time,3)
                if left_time <= 0:
                    self.timer.text = "Timeout!"
                else:
                    self.timer.text = f"{left_time:07.3f}"

        t = Thread(target=_start_timer)
        t.start()

    def build(self):
        self.layout.add_widget(self.title_)
        self.layout.add_widget(self.textinput)
        self.layout.add_widget(self.btn1)
        self.layout.add_widget(self.timer)
        return self.layout


if __name__ == '__main__':
    MyApp().run()