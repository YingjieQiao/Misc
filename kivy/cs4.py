from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button 
from kivy.uix.label import Label
from kivy.app import App
from kivy.core.window import Window 

class MenuScreen(Screen):
    def __init__(self, **kwargs):
        Screen.__init__(self, **kwargs)
        self.layout = BoxLayout()
        self.settings_button = Button(text="Settings"，on_press=self.change_to_setting())
        self.quit_button = Button(text="Quit", on_press=self.quit_app())
        
        self.layout.add_widget(self.settings_button)
        self.layout.add_widget(self.quit_button)
        
        self.add_widget(self.layout)
        # Add your code below to add the two Buttons
        pass

    def change_to_setting(self, value):
        self.manager.transition.direction = 'left'
        # modify the current screen to a different "name"
        self.manager.current = None

    def quit_app(self, value):
        App.get_running_app().stop()
        Window.close()


class SettingsScreen(Screen):
    def __init__(self, **kwargs):
        Screen.__init__(self, **kwargs)
        self.layout = BoxLayout()
        # Add your code below to add the label and the button
        self.settings_label = Label(text="Settings")
        self.menu_button = Button(text="Back to Menu")
        self.layout.add_widget(self.settings_label)
        self.layout.add_widget(self.menu_button)
        self.add_widget(self.layout)

    def change_to_menu(self, value):
        self.manager.transition.direction = 'right'
        # modify the current screen to a different "name"
        self.manager.current = None


class SwitchScreenApp(App):
    def build(self):
            sm = ScreenManager()
            ms = MenuScreen(name='menu')
            st = SettingsScreen(name='settings')
            sm.add_widget(ms)
            sm.add_widget(st)
            sm.current = 'menu'
            return sm


SwitchScreenApp().run()
