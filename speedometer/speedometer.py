from concurrent.futures.thread import ThreadPoolExecutor

from kivy.app import App
from kivy.properties import ObjectProperty, NumericProperty
from kivy.uix.widget import Widget

from listener import SpeedTCPListener, run_listener


class Pointer(Widget):
    angle = NumericProperty(0)

    def rotate(self, angle):
        self.angle = angle


class Speedometer(Widget):
    pointer = ObjectProperty(None)

    def change_speed(self, speed):
        self.pointer.rotate(speed)


class Dashboard(Widget):
    speedometer = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.speedometer.change_speed(90)


class SpeedometerApp(App):

    def build(self):
        dashboard = Dashboard()
        SpeedTCPListener.set_speedometer(dashboard.speedometer)
        return dashboard


if __name__ == '__main__':
    executor = ThreadPoolExecutor(2)
    executor.submit(run_listener)

    SpeedometerApp().run()
