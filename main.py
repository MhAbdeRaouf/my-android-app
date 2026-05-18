from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button


class RootWidget(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", padding=20, spacing=10, **kwargs)
        self.label = Label(text="Hello, Android!", font_size="24sp")
        self.button = Button(text="Press Me", size_hint=(1, 0.2))
        self.button.bind(on_press=self.on_button_press)
        self.add_widget(self.label)
        self.add_widget(self.button)

    def on_button_press(self, instance):
        self.label.text = "Button Pressed!"


class MyApp(App):
    def build(self):
        return RootWidget()


if __name__ == "__main__":
    MyApp().run()