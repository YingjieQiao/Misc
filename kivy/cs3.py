from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button 


class MyLabel(Label):

    def __init__(self, **kwargs):
        Label.__init__(self, **kwargs)
        self.bind(size=self.setter('text_size'))
        self.padding = (20, 20)
        self.font_size = 24
        self.halign='left'
        self.valign='middle'

class MyTextInput(TextInput):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.hint_text = "enter a value"
        self.input_filter = "float"
        self.fond_size = 72
        
class Investment(App):

    def build(self):
        layout = GridLayout(cols=2)
        l1 = MyLabel(text="Investment Ammount",)
        layout.add_widget(l1)
        
        self.input_amount = MyTextInput()
        layout.add_widget(self.input_amount)
        
        l2 = MyLabel(text="Years")
        layout.add_widget(l2)
        self.years = MyTextInput()
        layout.add_widget(self.years)
        
        l3 = MyLabel(text="Annual Interest Rate")
        layout.add_widget(l3)
        self.interest_rate = MyTextInput()
        layout.add_widget(self.interest_rate)
        
        l4 = MyLabel(text="Future Value")
        layout.add_widget(l4)
        self.txt_future_val = MyLabel(text="answer here")
        layout.add_widget(self.txt_future_val)
        
        btn = Button(text="Calculate", on_press=self.calculate, font_size=24)
        layout.add_widget(btn)
        return layout

    def calculate(self, instance):
        inv_amt = float(self.input_amount.text)
        years = float(self.years.text)
        mth_int_rate = float(self.interest_rate.text)/100
        future_value = inv_amt * (1+mth_int_rate)**(years*12)
        self.txt_future_val.text = "{:.2f}".format(future_value)



Investment().run()
