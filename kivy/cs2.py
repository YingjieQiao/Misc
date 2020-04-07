from kivy.app import App
from kivy.uix.label import Label


class SlideDetectApp(App):
    def build(self):
        self.label = Label(text="slide")
        self.label.bind(on_touch_move=self.detect)
        return self.label
    
    def detect(self, instance, touch):
        # if not instance.collide_point(touch.x, touch.y):
        #   return False
        print(touch.px)
        if touch.dx < -40:
            pass
        if touch.dx > 40:
            pass
        if touch.dy < -40:
            pass
        if touch.dy > 40:
            pass
        return True


SlideDetectApp().run()
