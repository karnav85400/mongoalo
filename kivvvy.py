from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class MyBoxLayout(BoxLayout):
    def __init__(self, **kwargs):
        super(MyBoxLayout, self).__init__(**kwargs)

        num1_input = TextInput(hint_text="Enter first number", size_hint=(0.3, None), height=50)
        num2_input = TextInput(hint_text="Enter second number", size_hint=(0.3, None), height=50)

        input_layout = BoxLayout(size_hint=(None, None), size=(500, 100), spacing=10, padding=10)
        input_layout.add_widget(num1_input)
        input_layout.add_widget(num2_input)

        result_label = Label(text="Result: ", size_hint=(0.3, None), height=50)

        calculate_button = Button(text="Calculate", size_hint=(0.3, None), height=50, on_press=lambda x:self.calculate(num1_input, num2_input, result_label))

        button_layout = BoxLayout(size_hint=(None, None), size=(500, 100), spacing=10, padding=10)
        button_layout.add_widget(result_label)
        button_layout.add_widget(calculate_button)

        main_layout = BoxLayout(orientation="vertical")
        main_layout.add_widget(Label(text="Enter Two Numbers", size_hint=(1, None), height=50))
        main_layout.add_widget(input_layout)
        main_layout.add_widget(button_layout)

        self.add_widget(main_layout)

    def calculate(self, num1_input, num2_input, result_label):
        try:
            num1 = int(num1_input.text)
            num2 = int(num2_input.text)
            result = num1 + num2
            result_label.text = "Result: " + str(result)
        except ValueError:
            result_label.text = "Result: Invalid input"

class MyKivyApp(App):
    def build(self):
        return MyBoxLayout()

if __name__ == "__main__":
    MyKivyApp().run()
