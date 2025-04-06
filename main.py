import kivy
from kivy.app import App

from timer_component.timer_model import TimerModel
from timer_component.timer_controller import TimerController
from common.logger import LoggerCreator


class MainApp(App):
    """
    Class based on Kivy's App, created to run the application and show TimerComponent.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # initialize attributes for timer
        self.timer_model = TimerModel()
        self.timer_controller = TimerController(self.timer_model)

    def build(self):
        return self.timer_controller.ui


if __name__ == '__main__':
    LoggerCreator.setup_default_logger()
    MainApp().run()