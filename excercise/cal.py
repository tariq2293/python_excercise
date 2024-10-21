from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label


class CalculatorApp(App):
    def build(self):
        self.title = "Sample Calculator"
        layout = GridLayout(cols=2)
        self.result = Label(text="Result: ")

        self.input1 = TextInput(hint_text='Enter first number', multiline=False)
        self.input2 = TextInput(hint_text='Enter second number', multiline=False)

        layout.add_widget(self.input1)
        layout.add_widget(self.input2)

        self.add_button = Button(text="Add")
        self.add_button.bind(on_press=self.add_numbers)
        layout.add_widget(self.add_button)

        self.sub_button = Button(text="Sub")
        self.sub_button.bind(on_press=self.sub_numbers)
        layout.add_widget(self.sub_button)

        self.mul_button = Button(text="Mul")
        self.mul_button.bind(on_press=self.mul_numbers)
        layout.add_widget(self.mul_button)

        self.div_button = Button(text="Div")
        self.div_button.bind(on_press=self.div_numbers)
        layout.add_widget(self.div_button)

        layout.add_widget(self.result)

        return layout

    def add_numbers(self, instance):
        try:
            num1 = float(self.input1.text)
            num2 = float(self.input2.text)
            result = num1 + num2
            self.result.text = f"Result: {result}"
        except ValueError:
            self.result.text = "Invalid input!"

    def sub_numbers(self, instance):
        try:
            num1 = float(self.input1.text)
            num2 = float(self.input2.text)
            result = num1 - num2
            self.result.text = f"Result: {result}"
        except ValueError:
            self.result.text = "Invalid input!"

    def mul_numbers(self, instance):
        try:
            num1 = float(self.input1.text)
            num2 = float(self.input2.text)
            result = num1 * num2
            self.result.text = f"Result: {result}"
        except ValueError:
            self.result.text = "Invalid input!"

    def div_numbers(self, instance):
        try:
            num1 = float(self.input1.text)
            num2 = float(self.input2.text)
            if num2 != 0:
                result = num1 / num2
                self.result.text = f"Result: {result:.2f}"
        except ValueError:
            self.result.text = "Invalid input!"


if __name__ == '__main__':
    CalculatorApp().run()
