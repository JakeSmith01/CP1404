from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

MILES_TO_KM = 1.60934


class MilesToKilometresConverter(App):

    def build(self):
        Window.size = (600, 400)
        self.title = "Miles to Kilometres Converter"
        self.root = Builder.load_file('m_to_k_converter.kv')
        return self.root

    def handle_conversion(self):
        miles = self.test_input_validity()
        kilometres = miles * MILES_TO_KM
        self.root.ids.output_number.text = str(kilometres)

    def handle_change(self, change):
        increment = self.test_input_validity() + change
        self.root.ids.input_number.text = str(increment)
        self.handle_conversion()

    def test_input_validity(self):
        try:
            value = float(self.root.ids.input_number.text)
            return value
        except ValueError:
            return 0


MilesToKilometresConverter().run()
