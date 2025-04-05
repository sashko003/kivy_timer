import kivy
from kivy.app import App

from timer_component.timer_model import TimerModel
from timer_component.timer_controller import TimerController


class MainApp(App):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.timer_model = TimerModel()
        self.timer_controller = TimerController(self.timer_model)

    def build(self):
        return self.timer_controller.ui


if __name__ == '__main__':
    MainApp().run()