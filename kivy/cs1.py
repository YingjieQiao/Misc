import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.interactive import InteractiveLauncher


class AlternateApp(App):

    def build(self):
        self.label = Label(text="Programming is fun")
        self.label.bind(on_touch_down=self.alternate)
        self.state = 0
        return self.label

    def alternate(self, instance, touch):
        if self.state == 0:
            self.label.text = "It is fun to program"
            self.state = 1
        else:
            self.label.text = "Programming is fun"
            self.state = 0
            
myapp = AlternateApp()
myapp.run()
